# ---------IMPORTED COMPONENTS---------
# define imports for required functions in script
import requests
from hashlib import new
from todoist_api_python.api import TodoistAPI
from decouple import config

# ---------ENVIRONMENT VARS---------
# TODOIST_ENVs
# api key defined in operating system variables
todoist_api_key = config('TODO_API_KEY', '')
# debugging api_key status
assert todoist_api_key, 'TODO_API_KEY not set!'

# TRELLO_ENVs
# api key defined in operating system variables
trello_api_key = config('TRELLO_API_KEY', '')
assert trello_api_key, 'TRELLO_API_KEY not set!'  # debugging api_key status
# api token defined in operation system variables
trello_api_token = config('TRELLO_API_TOKEN', '')
assert trello_api_token, 'TRELLO_API_TOKEN not set!'  # debugging api_key status

# ------TRELLO API---------
# api url
trello_api_url = 'https://api.trello.com/1'


# ------TODOIST API---------
# imported TodoistAPI component
todoist_api = TodoistAPI(todoist_api_key)
# inserting api_key var into Todoist api_url
todoist_api_url = 'https://api.todoist.com/rest/v1/tasks?token='+todoist_api_key


# ---------GET TODOIST TASKS FUNCTION---------
# define custom 'get_todoist_tasks' function to obtain the tasks from Todoist
# accepts 'due' param string which is a due-date(imported from 'TodoistAPI')
# also accepts a boolean value -> if this param is specified it will only return the response code for debugging purposes
def get_todoist_tasks(due, res_code=False):
    # get tasks request to TodoistAPI component requesting to filter by duedate
    todoist_tasks = todoist_api.get_tasks(filter=due)
    # get todoist api_url and store response code in variable for debugging purposes
    todoist_res_code = requests.get(todoist_api_url)

    if res_code:
        return todoist_res_code
    else:
        # if an empty project list is returned, return False
        if todoist_tasks == []:
            return False
        # # else the project list for today's todos is returned
        else:
            return todoist_tasks


# ---------ARCHIVE TASKS FUNCTION---------
# define custom 'archive_tasks' function to archive all Trello tasks in the specific Trello list before POST function


def archive_tasks():
    # trello list/cards endpoint
    trello_endpnt = '/lists/62e76990eea21e6558161fb9/archiveAllCards'
    # full GET url pointing to the api list/{listID}/cards endpoint to obtain a list of all cards in Trello list
    trello_list_cards_url = trello_api_url+trello_endpnt

    # query the trello lists/{id}/archiveAllCards endpoint
    query = {
        'key': trello_api_key,
        'token': trello_api_token
    }

    # make a post request to the endpoint with the above query
    response = requests.post(trello_list_cards_url, params=query)
    assert 200 <= response.status_code < 400, 'Failed to archive_tasks, ERROR: '+response.text
    return response
# ---------POST TASKS FUNCTION---------
# define custom 'post_tasks' function to accept task_name and label from get_tasks function and create cards on the Trello board


def post_tasks(task_name, label):
    # trello cards endpoint
    trello_endpnt = '/cards'
    # full POST url pointing to the api /cards endpoint to create the cards
    trello_cards_url = trello_api_url+trello_endpnt

    # query the trello /cards endpoint
    query = {
        'idList': '62e76990eea21e6558161fb9',
        'key': trello_api_key,
        'token': trello_api_token,
        'name': task_name,
        'idLabels': label
    }
    # json response object creating a trello card with the parameter values specified in the query
    response = requests.post(trello_cards_url, params=query)
    assert 200 <= response.status_code < 400, 'Failed to post_tasks, ERROR: '+response.text
    return response
# ---------OUTPUT FILE FUNCTION---------
# define custom 'wrt_file' function to accept string and write to external file


def wrt_file(text):
    # open the external file and write to the file
    with open('../../../../OneDrive/output.txt', 'w') as external_file:
        # print string to the external file
        print(text, file=external_file)
        # save and close the external file
        external_file.close()


# ---------MAIN APP FUNCTION--------
# define 'main_app' function to control outcome of the script
 # accepts sick_day boolean to allow for hardcoded boolean value to prevent futher execution
 # accepts clear_tasks boolean, which will ONLY archive all tasks then exit the script
def main_app(sick_day=False, clear_tasks=False):
    # VARIABLES FOR MAIN_APP FUNCTION
    # Good morning text string, written to the start of the output file
    good_morn_text = 'Good Morning Team! :sun: \n\n-----Todo\'s for today-----\n'
    # trello label_ids
    trello_label_today = ['62e7967dc8e1c38fa2332360']
    # get the todoist tasks object
    todoist_task_obj = get_todoist_tasks('(today | overdue)')
    # get the todoist response object
    todoist_res_obj = get_todoist_tasks('(today | overdue)', True)

    # if the clear_tasks param is set to True, archive all Trello cards in the list
    if clear_tasks:
        archive_tasks()
    # else proceed with executing the below code
    else:
        # if the sick_day param is NOT set, proceed with running the below code
        if not sick_day:
            # if the get_todoist_tasks function returns false, meaning no tasks were returned from the request, the below string is outputted to the output.txt file
            if not todoist_task_obj:
                archive_tasks()
                wrt_file(
                    'Oops someone forgot to add tasks the todo list...'+str(todoist_res_obj))
            # if there is a JSON object with values the main code executes
            else:
                # ADDITIONAL VARIABLES FOR MAIN_APP FUNCTION
                # return length of number of items in todoist_task_obj
                todoist_task_count = range(len(todoist_task_obj))
                # output todoist tasks to joint string in output.txt
                output_txt = good_morn_text + \
                    '\n'.join(str(todoist_task_obj[x].content)
                              for x in todoist_task_count)
                # Archive all cards in trello list
                archive_tasks()
                # POST each 'new' task to Trello with the label 'Todo: Today'
                # then, write Todoist tasks to output.txt file
                [post_tasks(todoist_task_obj[x].content, trello_label_today)
                 for x in todoist_task_count]
                wrt_file(output_txt)


# call the main_app function to write tasks from Todoist to Trello and write the Todoist tasks to the output.txt file
main_app()

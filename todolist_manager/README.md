<p>
    They said move to Trello for my todo-lists. So I did… but with automation 🦾 😉 🦿
    <br>
</p>

![automated](https://user-images.githubusercontent.com/61925456/184543935-d5c72299-4fc3-4072-a063-6c3c15d8ba52.gif)

<h2><strong>Background:</strong></h2>
<p>I primarily use an application called Todoist, which, in-short, is a Todo-List management application. However, my company decided to move to Trello, and maintain Todo-Lists within Trello Cards. So I adapted with the magic of Python3. Feel free to read how this works below.</p>

<h2><strong>How it Works:</strong></h2>
<p>
    This script will first check for parameters, such as; is there existing tasks to-do, is there an issue returning the Todoist task? Then once all passed, the function proceeds to archive all existing Trello Cards within a specific list ID and POST the outstanding Todoist tasks to Trello, creating a Trello Card for each outstanding Todoist task with the specified Trello List.  
    <br>
    <br>
    Additionally, I have today’s tasks from Todoist written to an output file formatted in a nice morning greeting, which is automatically synced by my One Drive each morning. 
    <br>
    <br>
    This means I can work from the safety of my Todoist app and know that in the back of my mind that my tasks for the day will be copied across to Trello daily - keeping everyone updated, and avoiding double-handling. 
    
</p>

<h2><strong>Disclaimer:</strong></h2>
<p>The environment variables and both the Todoist/Trello instances are all privated as this was a personal project, however, if you would like a demo of how this works, please feel free to reach out to me via the social links provided on my Github profile README.</p>

[![Github - Kyle's Profile](https://img.shields.io/badge/Github-Kyle's_Profile-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zero2164)

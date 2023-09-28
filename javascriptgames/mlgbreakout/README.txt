Special Thanks to 
https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript
for providing the tutorial necessary to complete this project.

This project is for ETSU's ACM Game Jam Spring 2023.
It lasted from late February to late March.
I worked on this project from March 9,2023 to March 20, 2023.

THEME: Time is Power.
It's Breakout, but MLG.
(Less) Time is Power!

How does this project fit the theme?
- At first, the hitsounds sound weak. They're little taps.
- As the ball speeds up, more hitsounds happen, and they hit HARDER!
- Faster completion means more power. Hence, (less) time is power.

This project took about 2 weeks of spare time to complete.
It was fun. But it became even MORE fun when I made it UNIQUE!

Why I chose JavaScript
	- Back in High School, JavaScript was my first coding language (actually HTML, but ignore that).
	- I remember making a cave helicopter game using JavaScript.
	- I am currently learning (more) JavaScript in Advanced Topics in Web Development.
	- I would like to inspire myself by creating this project.

What I learned completing this project:
	- How to make GAMES using JAVASCRIPT!!!
	- How to use <script> tags in JavaScript.
	- The basic layout of an HTML page (again).
	- Creating a canvas.

	- How to add, get, and play mp3 files using HTML DOM's Audio method.
		- https://www.w3schools.com/jsref/met_audio_play.asp
	- Some other methods and classes provided by the HTML Document Object Model.
	- Reinforcing my knowledge of JavaScript using document.getElementById();
		- By the way, getting elements like this seems to be more OP than instructors tell students.

	- Event Listeners (Mouse Input and Keyboard Input)
	- AND MORE!


What I got from completing this project:
	- More knowledge about JavaScript
	- A cool website to show off my MLG coding skills.
	- Practical use of my Physics knowledge from my Physics class.
 



Resources Used:
Coding Help:
	Basic Structure of the Breakout Game:
		https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript

	Image() Documentation:
		https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image

	Drawing an Image onto a Canvas
		https://www.w3schools.com/tags/canvas_drawimage.asp
	
	Audio() Documentation:
		https://www.w3schools.com/jsref/met_audio_play.asp

	Detecting Middle Click
		https://stackoverflow.com/questions/21224327/how-to-detect-middle-mouse-button-click

	Getting the Width of Text in the Canvas
		https://stackoverflow.com/questions/118241/calculate-text-width-with-javascript

	Displaying a Video in the Canvas
		https://stackoverflow.com/questions/4429440/html5-display-video-inside-canvas

	Adding a video to the canvas.
		https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Manipulating_video_using_canvas

	

Music:
	https://youtu.be/2gIViY655Og - Sniper Sound provided by Peyton gaming
	https://youtu.be/HHprqoH1EeU - Hitmarker Sound provided by trottski16
	https://youtu.be/Cserwt5jvHg - Background music provided by No Copyright Background Music


Video:
	https://youtu.be/4bjliCePDXY - Sniper Green Screen provided by MSP - XBoysX
	

Online Tools:
	https://www.bestmp3converter.com/ 	- Converting the Music above (provided by YouTube) into MP3 Files.
	https://mp3cut.net/		    		- Editing Music down to reduce audio length and size.
	https://iyoutubetomp4.com/en2/		- Converting the YouTube video into an MP4 File.
	https://cloudconvert.com/mp4-to-gif - Converting an MP4 File to a GIF.
	https://www.bestmp3converter.com/	- Converting an MP4 to MP3.


Free Software Used:
	Clip Champ		- Video Editor provided by Windows 11.

(Intentional) Bugs:
The ball sometimes doesn't bounce off bricks correctly.
	- PWN Mode allows the ball to ignore Newton's 3rd Law and blaze through bricks!
	- A fast enough speed causes the ball to bounce left-right instead of up-down (time is power!).
	- Snipe Mode happens when there are less than 1/8 of bricks remaining. (time is power!)
		
The paddle gets larger after some time
	- this is an intentional mechanic to improve the gameplay.

The green screen when the ball hits a brick in snipe Mode
	- I have tried to fix this bug, but it was not worth it.
	- Every solution I tried threw a cross-origin error that I couldn't fix OR
	- it left the video in a black screen.




Version History

	Version 1.0
	- Stable version of project. 
	- Contained basic breakout functionality with background, hitmarkers, hitmarker audio, and automode/pwnMode/snipeMode.

	Version 1.2
	- Branches off Version 1.0 to add more features.
	
		Features
		- Includes additions to SnipeMode, adding a video overlay "sniping" the brick upon collision.
		- Added Wombo Combo effect. Whenever you hit more than 10 bricks with 1 paddle bounce, you get the wombo combo sound.
			- Don't worry - Wombo Combo is easy to achieve.
		- Added Colorblind mode to remove the background image.
			- Activate it by pressing C.

		Bug Fixes
		- Fixed bugs with pausing the game - it didn't actually pause the game.
	
		Code Changes
		- Added comments as much as possible. This project should be understood by rookies to JavaScript.
		- Rearranged functions and code to appropriate locations under comment headers.
		- Updated the index.html file comment header to include the version. 
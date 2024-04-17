 Imports:tkinter: For GUI development.
PIL: To handle and display images.
randint: To generate random integers for computer's choice.
Initialize Tkinter:Tk(): Creates the main window.
title(): Sets the title of the window.
config(): Configures the background color of the window.
 Setting Window Icon: Setting Window Icon:
 Load Images: Load images for user and computer choices.
 Create Labels for Images and Scores: Label: Widgets to display images and scores.
 Grid Layout: grid(): Arranges widgets in a grid.
 Indicators and Message Label:  Widgets for indicating user and computer, and displaying messages.
 Function Definitions: updateMessage(): Updates the message label.
updateUserScore(): Updates the user's score.
updateCompScore(): Updates the computer's score.
winner_check(): Checks the winner based on choices.
choice_update(): Updates the game based on player's choice.
Buttons: : Widgets to take user input for choices and to play again.
Main Loop: mainloop(): Runs the application.

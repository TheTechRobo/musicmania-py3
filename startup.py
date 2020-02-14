print("Welcome to Anglemania!")
print()
def load():
   guicli = raw_input('''Would you like a graphical interface or a text interface? (gui/cli, case-sensitive)
   Type:''')
   if guicli == "gui":
      print("Loading...")
      try:
          execfile('python gui.py')
      except KeyboardInterrupt:
          print("You exited the program.")
          exit()
      except IOError:
          print("Error in finding files, do they exist?")
          print("(By default the terminal is in your home folder ~. Try cd'ing to the dir that Anglemania is in.)")
      except:
          print("An unrecognized error occured.")
   elif guicli == "cli":
      #print("Okay, loading...")
      #execfile('python cli.py')
	  print("Unfortunatley the text-based version hasn't been programmed yet :(")
	  exit()
   else:
      print("Please type either gui or cli, case-sensitive (gui is graphical, cli is text")
      load()
load()
print("Thanks for using Anglemania!")
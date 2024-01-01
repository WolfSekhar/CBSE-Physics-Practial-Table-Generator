from rich.console import Console
import xii.series_meter_bridge as Series
import xii.parallel_meter_bridge as Parallel
import xii.resistance_of_wire as ResistanceOfWire
import xii.resistivity_vi as ResistivityOfWire
import xii.galvanometer_half_deflection as GHalfDeflection
import xii.galvanometer_to_voltmeter as GTV
import xii.concave_mirror_focal_length as CMF
import art as art

class Main():
	def __init__(self):
		self.experiments = {}
		self.console = Console()
		self.number_of_experiment = 0
		self.importAllExperimentsWithPath()

	def importAllExperimentsWithPath(self):
		self.experiments[1] = ("To determine resistivity of two / three wires " +
		 " by plotting a graph for potential difference versus current.")
		self.experiments[2] = (("To find resistance of a given wire / standard resistor using metre bridge."))
		self.experiments[3] =("To verify the laws of combination (series) of resistances using a metre bridge.")
		self.experiments[4] = ("To verify the laws of combination (parallel) of resistances using a metre bridge.")
		self.experiments[5] = ('To determine resistance of a galvanometer by half-deflection method and to find its'+
			'figure of merit')
		self.experiments[6] = ("To convert the given galvanometer (of known resistance and figure of merit) into a " +
			"voltmeter of desired range and to verify.")
		self.experiments[7] = ("To find the value of v for different values of u in case of a concave mirror and to find the focal length.")


	def showOptions(self):
		self.console.print("Choose Experiment : ", style="red")
		for exp in self.experiments:
			self.console.print(str(exp) + " : ",end= '')
			self.console.print("[#af8787]"+self.experiments.get(exp))
	def takeInput(self):
		input_experiment_number = input("Enter the experiment number : ")
		
		try: 
			self.number_of_experiment = int(input_experiment_number)
			self.console.print(input_experiment_number)
		except ValueError:
			self.console.print("ERROR")
		

	def showTabulation(self,experiment_number):
		if experiment_number == 3:
			Series.Series().run()
		elif experiment_number == 4:
			Parallel.Parallel().run()
		elif experiment_number == 2:
			ResistanceOfWire.ResistanceOfWire().run()
		elif experiment_number == 1:
			ResistivityOfWire.ResistivityOfWires().run()
		elif experiment_number == 5:
			GHalfDeflection.GalvanometerHalfDeflection().run()
		elif experiment_number == 6:
			GTV.GalvanometerToVoltmeter().run()
		elif experiment_number == 7:
			CMF.ConcaveMirror().run()
		else:
			exit()


	def test(self):
		for i in range(2):
			s = Series.Series()
			s.run()

	def closeProgramAlert(self):
		self.console.print("\n\n [bold red] PRESS ENTER TO CLOSE THE PROGRAM : ")

	def showAuthor(self):
		self.console.print("[bold bright_magenta]PHYSICS PRACTICAL TABLE GENERATOR",justify = "center")
		self.console.print(art.text2art("PHY - P - GEN",chr_ignore=False))
		self.console.print("[b] By : [b blue]P.SEKHAR [white]([#87d700 b]PGT PHYSICS[white])",justify = "center")
		self.console.print("[b]contact : [b #5f87d7] sekhar.root@gmail.com",justify = "center")
		self.console.print("[b] url : [b #00ff00]https://github.com/WolfSekhar",justify = "center")






main = Main()
main.showAuthor()
main.showOptions()
main.takeInput()
main.showTabulation(main.number_of_experiment)
main.closeProgramAlert()
input(" ")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder 


Builder.load_file("calc.kv")



class Root(Widget	):
	def clear(self):
		self.ids.score.text = "0"
		self.ids.score.color = "000000"


	def button_press(self, button):
		prior = self.ids.score.text 
		if "Error" in prior:
			prior = ''
		if prior == "0":
			self.ids.score.text = ''
			self.ids.score.text = f'{button}'
		else:
			self.ids.score.text = f'{prior}{button}'


	def add_sign(self):
		prior = self.ids.score.text
		if prior[-1] == "-" or prior[-1] == "+"  or prior[-1] == "/" or prior[-1] == "*":
			pass
		else:
			self.ids.score.text = f"{prior}+"



	def subtract_sign(self):
		prior = self.ids.score.text
		if prior[-1] == "-" or prior[-1] == "+"  or prior[-1] == "/" or prior[-1] == "*":
			pass
		else:
			self.ids.score.text = f"{prior}-"

	def multiply_sign(self):

		prior = self.ids.score.text
		if prior[-1] == "/" or prior[-1] == "+"  or prior[-1] == "-" or prior == "**" :
			pass
		elif "**"  in prior:
			pass
		else:
			self.ids.score.text = f"{prior}*"


	def divide_sign(self):
		prior = self.ids.score.text
		if prior[-1] == "-" or prior[-1] == "+"  or prior[-1] == "/" or prior[-1] == "*":
			pass
		else:
			self.ids.score.text = f"{prior}/"

	def dot(self):
		prior = self.ids.score.text
		num_list = prior.split("+")

		if "+" in prior and "." not in num_list[-1]:	
			prior = f'{prior}.'
			self.ids.score.text = prior			
		elif "." in prior:
			pass
		else:
			prior = f'{prior}.'
			self.ids.score.text = prior	



	def equals(self):

		try : 

			allowed = ["0","1","2","3","4","5","6","7","8","9","+","-","/","*","%","."]

			prior = self.ids.score.text
			prior = list(prior)
			for i in prior:
				if i not in allowed:
					self.ids.score.text = "0"
				else:
					answer = eval(self.ids.score.text)
					self.ids.score.text = str(answer)
		except:
			self.ids.score.text = "Eroor"

	def remove(self):
		prior = self.ids.score.text
		prior = prior[:-1]
		self.ids.score.text = prior


	def pos_neg(self):
		prior = self.ids.score.text
		if "-" in prior[0]:
			self.ids.score.text = f'{prior.replace("-","")}'
		else:
			self.ids.score.text = f'-{prior}'
class Calculator(App):
	def build(self):
		self.icon = "icon.png"
		return Root()



if __name__ == '__main__':
	Calculator().run()

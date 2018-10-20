#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, threading, time, rospy
from prius_msgs.msg import Control
from visualstates.codegen.python.state import State
from visualstates.codegen.python.temporaltransition import TemporalTransition
from visualstates.codegen.python.conditionaltransition import ConditionalTransition
from visualstates.codegen.python.runtimegui import RunTimeGui
from PyQt5.QtWidgets import QApplication


class GlobalNamespace():
	def __init__(self):
		rospy.init_node("prius_spawn", anonymous=True)

		self.priusPub = rospy.Publisher("/prius", Control, queue_size=10)
		time.sleep(1) # wait for initialization of the node, subscriber, and publisher

	def stop(self):
		rospy.signal_shutdown("exit ROS node")

	def publishprius(self, prius):
		self.priusPub.publish(prius)



class State0(State):
	def __init__(self, id, initial, globalNamespace, namespace, cycleDuration, parent=None, gui=None):
		State.__init__(self, id, initial, cycleDuration, parent, gui)
		self.globalNamespace = globalNamespace
		self.namespace = namespace

	def runCode(self):
		pass


class Namespace0():
	def __init__(self, globalNamespace):
		self.globalNamespace = globalNamespace


class State1(State):
	def __init__(self, id, initial, globalNamespace, namespace, cycleDuration, parent=None, gui=None):
		State.__init__(self, id, initial, cycleDuration, parent, gui)
		self.globalNamespace = globalNamespace
		self.namespace = namespace

	def runCode(self):
		pass


class Namespace1():
	def __init__(self, globalNamespace):
		self.globalNamespace = globalNamespace


class State2(State):
	def __init__(self, id, initial, globalNamespace, namespace, cycleDuration, parent=None, gui=None):
		State.__init__(self, id, initial, cycleDuration, parent, gui)
		self.globalNamespace = globalNamespace
		self.namespace = namespace

	def runCode(self):
		command = Control()
		command.throttle = 0.8
		command.brake = 0
		command.steer = 0.4
		self.globalNamespace.publishprius(command)


class Namespace2():
	def __init__(self, globalNamespace):
		self.globalNamespace = globalNamespace


class State3(State):
	def __init__(self, id, initial, globalNamespace, namespace, cycleDuration, parent=None, gui=None):
		State.__init__(self, id, initial, cycleDuration, parent, gui)
		self.globalNamespace = globalNamespace
		self.namespace = namespace

	def runCode(self):
		command = Control()
		command.throttle = 1
		command.brake = 0
		command.steer = -0.7
		self.globalNamespace.publishprius(command)
		
class Namespace3():
	def __init__(self, globalNamespace):
		self.globalNamespace = globalNamespace


class State4(State):
	def __init__(self, id, initial, globalNamespace, namespace, cycleDuration, parent=None, gui=None):
		State.__init__(self, id, initial, cycleDuration, parent, gui)
		self.globalNamespace = globalNamespace
		self.namespace = namespace

	def runCode(self):
		command = Control()
		command.throttle = 1
		command.brake = 0
		command.steer = 0
		self.globalNamespace.publishprius(command)


class Namespace4():
	def __init__(self, globalNamespace):
		self.globalNamespace = globalNamespace


class State5(State):
	def __init__(self, id, initial, globalNamespace, namespace, cycleDuration, parent=None, gui=None):
		State.__init__(self, id, initial, cycleDuration, parent, gui)
		self.globalNamespace = globalNamespace
		self.namespace = namespace

	def runCode(self):
		command = Control()
		command.throttle = 0
		command.brake = 1
		command.steer = 0
		self.globalNamespace.publishprius(command)


class Namespace5():
	def __init__(self, globalNamespace):
		self.globalNamespace = globalNamespace


class Tran1(TemporalTransition):

	def runCode(self):
		pass

class Tran2(TemporalTransition):

	def runCode(self):
		pass

class Tran3(TemporalTransition):

	def runCode(self):
		pass

displayGui = False
guiThread = None
gui = None

def readArgs():
	global displayGui
	for arg in sys.argv:
		splitedArg = arg.split('=')
		if splitedArg[0] == '--displaygui':
			if splitedArg[1] == 'True' or splitedArg[1] == 'true':
				displayGui = True
				print('runtime gui enabled')
			else:
				displayGui = False
				print('runtime gui disabled')

def runGui():
	global gui
	app = QApplication(sys.argv)
	gui = RunTimeGui()
	gui.show()
	app.exec_()

if __name__ == "__main__":

	globalNamespace = GlobalNamespace()


	readArgs()
	if displayGui:
		guiThread = threading.Thread(target=runGui)
		guiThread.start()


	if displayGui:
		while(gui is None):
			time.sleep(0.1)

		gui.addState(0, "root", True, 0.0, 0.0, None)
		gui.addState(1, "SpawnPrius", True, 977.0, 911.0, 0)
		gui.addState(2, "SteerLeft", True, 988.0, 839.0, 1)
		gui.addState(3, "SteerRight", False, 1189.0, 834.0, 1)
		gui.addState(4, "MoveForward", False, 1196.0, 1012.0, 1)
		gui.addState(5, "Stop", False, 1001.0, 1014.0, 1)

		gui.addTransition(1, "transition 1", 2, 3, 1088.5, 836.5)
		gui.addTransition(2, "transition 2", 3, 4, 1192.5, 923.0)
		gui.addTransition(3, "transition 3", 4, 5, 1098.5, 1013.0)

	if displayGui:
		gui.emitLoadFromRoot()
		gui.emitActiveStateById(0)

	namespace0 = Namespace0(globalNamespace)
	state0 = State0(0, True, globalNamespace, None, 100, None, gui)
	namespace1 = Namespace1(globalNamespace)
	state1 = State1(1, True, globalNamespace, namespace0, 100, state0, gui)
	namespace2 = Namespace2(globalNamespace)
	state2 = State2(2, True, globalNamespace, namespace1, 100, state1, gui)
	namespace3 = Namespace3(globalNamespace)
	state3 = State3(3, False, globalNamespace, namespace1, 100, state1, gui)
	namespace4 = Namespace4(globalNamespace)
	state4 = State4(4, False, globalNamespace, namespace1, 100, state1, gui)
	namespace5 = Namespace5(globalNamespace)
	state5 = State5(5, False, globalNamespace, namespace1, 100, state1, gui)

	tran1 = Tran1(1, 3, 2000)
	state2.addTransition(tran1)

	tran2 = Tran2(2, 4, 1000)
	state3.addTransition(tran2)

	tran3 = Tran3(3, 5, 1000)
	state4.addTransition(tran3)

	try:
		state0.startThread()
		state1.startThread()
		state0.join()
		state1.join()
		globalNamespace.stop()
		sys.exit(0)
	except:
		state0.stop()
		state1.stop()
		if displayGui:
			gui.close()
			guiThread.join()

		state0.join()
		state1.join()
		globalNamespace.stop()
		sys.exit(1)

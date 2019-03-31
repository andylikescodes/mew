import numpy as np
import matplotlib.pyplot as plt

class EEG:
	def __init__(self, signals, ch_names, sampling_rate):
		"""
		Initializing the EEG signal in a better structure for analysis
		signals: a numpy array with channels x time
		ch_names: channel names
		sampling rate: sampling rate
		"""
		self.signals = {}
		self.sampling_rate = sampling_rate
		for i in range(len(ch_names)):
			self.signals[ch_names[i]] = signals[i]

		self.shape = signals.shape
		self.times = np.arange(self.shape[1])/self.sampling_rate

	def ch_names(self):
		return self.signals.keys()

	def get_channels(self, ch_names):
		channels = []
		for channel in ch_names:
			channels.append(self.signals[channel])
		np_channels = np.vstack(channels)
		return np_channels

	def plot(self, ch_name, signal_range):
		plt.plot(self.times[signal_range[0]:signal_range[1]], 
			self.signals[ch_name][signal_range[0]:signal_range[1]])
		plt.title('Channel: ' + ch_name + 
			' Range: ' + str(signal_range[0]/self.sampling_rate) + 
			'-' + str(signal_range[1]/self.sampling_rate) + 's')
		plt.xlabel('Time')
		plt.ylabel('Voltage')

	def power_spectrum():
		pas


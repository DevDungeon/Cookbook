require 'ruby-audio'
include RubyAudio

sample_rate = 48000
len = 10   # 10 seconds
freq = 440 # Play the A note
amp = 0.9  # Almost full volume

# The sample_rate dictates how many samples (or data points) make up
# ONE SECOND of audio. To get 10 seconds of data points we multiply
# our duration by the sample_rate.
buf = Buffer.float(sample_rate * len)
buf.size.times do |i| # for each data point
  sine_rad = ((freq * Math::PI * 2) / sample_rate) * i
  buf[i] = amp * Math.sin(sine_rad)
end

# Create the .wav file and write it with our buffer
format = FORMAT_WAV | FORMAT_PCM_16
info = SoundInfo.new(channels: 1, samplerate: sample_rate, format: format)
snd = Sound.new('out.wav', 'w', info)
snd.write(buf)
snd.close
require 'ruby-audio'

buf = RubyAudio::Buffer.float(1000)
out = nil
['out.wav', 'out.wav', 'out.wav'].each do |file|
  RubyAudio::Sound.open(file) do |snd|
    out = RubyAudio::Sound.open('out2.wav', 'w', snd.info.clone) if out.nil?

    while snd.read(buf) != 0
      out.write(buf)
    end
  end
end
out.close if out

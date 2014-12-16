#!/usr/bin/liquidsoap -v

set("log.file.path","/var/log/liquidsoap/fmr.log")
set("log.stdout",true)
set("log.file",true)
set("frame.audio.samplerate",44100)

%include "fmr.motor"

# Et on envoie
output.alsa(default)
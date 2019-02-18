import wave
import os
import hashlib
import datetime
import pyloudnorm as pyln
import soundfile as sf

def GetFileMD5Hash(path_to_wav):

    try:
        with open(path_to_wav, "rb") as f:
            contents = f.read()
        m = hashlib.md5(contents).hexdigest()
        return m
    except Exception as e:
        return "CRC Generation Error"

def get_bitrate(wave_obj:wave.Wave_read):
    framerate = wave_obj.getframerate()
    num_channels = wave_obj.getnchannels()
    sample_width = wave_obj.getsampwidth()

    bitrate = (framerate * num_channels * sample_width) / 1000

    return bitrate

def get_lufs_loudness(path_to_wav):

    data, rate = sf.read(path_to_wav) # load audio (with shape (samples, channels))
    meter = pyln.Meter(rate, block_size=0.100) # create BS.1770 meter
    loudness = meter.integrated_loudness(data) # measure loudness

    return loudness

def get_filecreationdate(path_to_wav):
    filecreationdate = \
        datetime.datetime.fromtimestamp(
            os.path.getctime(path_to_wav)
        )
    return filecreationdate

def get_wav_metadata(path_to_wav):

    is_valid_path = os.path.exists(path_to_wav)
    is_wav_file = path_to_wav.endswith('.wav')

    if is_valid_path and is_wav_file:

        wave_obj = wave.open(path_to_wav)

        metadata = {

            'bitrate' : get_bitrate(wave_obj),

            'lufs' : get_lufs_loudness(path_to_wav),

            'channels' : wave_obj.getnchannels(),

            'length' : wave_obj.getnframes() / wave_obj.getframerate(),

            'samplerate' : wave_obj.getframerate(),

            'crc' : GetFileMD5Hash(path_to_wav),

            'filecreationdate' : get_filecreationdate(path_to_wav),

            }
    
        return metadata


    
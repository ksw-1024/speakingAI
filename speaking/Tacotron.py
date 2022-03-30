from ttslearn.tacotron import Tacotron2TTS
from tqdm.notebook import tqdm
from IPython.display import Audio

engine = Tacotron2TTS()
wav, sr = engine.tts("一貫学習にチャレンジしましょう！", tqdm=tqdm)
Audio(wav, rate=sr)
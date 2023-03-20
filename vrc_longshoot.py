import modules
import time
import datetime

app_version = 5
options = modules.options_io.load(app_version)
print('options loaded.')
print(options)

#prepare recording
modules.get_image.init()
modules.window_handler.set_target_name(options['capture']['target'])

start_time = time.time()
if options['capture']['resize']:
    modules.window_handler.set_size(options['capture']['target'], {'x': 0, 'y':0}, options['capture']['size'])
else:
    modules.window_handler.focus(options['capture']['target'])
time.sleep(0.20)

capture_frames = int(options['capture']['fps'] * options['capture']['seconds'])
requred_delay = 1.0 / options['capture']['fps']
need_focused = options['capture']['force_focused']
##cache to run functions faster
mwh = modules.window_handler
mgi = modules.get_image

print('capture started. DO NOT MOVE TARGET WINDOW.')

try:
    for i in range(capture_frames):
        if need_focused:
            if not mwh.still_focused():
                print('target un-focused. stop recording.')
                break
        frame_start = time.time()
        mgi.add_frame()
        frame_elapsed = time.time() - frame_start
        time_2_wait = requred_delay - frame_elapsed
        if time_2_wait > 0:
           time.sleep(time_2_wait)
except KeyboardInterrupt:
    pass

print('recording_time:' + str(time.time() - start_time))


now = datetime.datetime.now()
nows = now.strftime('%Y-%m-%d_%H-%M-%S')
subdir = ""
if options['save']['monthly_subdir']:
    subdir = now.strftime('%Y-%m/')
modules.get_image.ensure_dir(f"{options['save']['folder']}{subdir}")
size = modules.get_image.get_size()

file_name = f'{options["save"]["folder"]}{subdir}{options["save"]["prefix"]}_{nows}_{size["width"]}x{size["height"]}.png'
modules.get_image.write(file_name, options['save']['make_bright'])

print('total_elapsed:' + str(time.time() - start_time))

if __file__.endswith('.py'):
    print("")
    input("hit any key to exit...")
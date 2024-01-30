from PIL import Image
import os

def analyseImage(path):
    """
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode
    before processing all frames.
    """
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }

    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break

            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


def processImage(path, output_folder):
    """
    Iterate the GIF, extracting each frame.
    """
    mode = analyseImage(path)['mode']
    gif = Image.open(path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for frame_number in range(gif.n_frames):
        gif.seek(frame_number)
        frame = gif.convert("RGBA")

        adjusted_frame_number = (frame_number - 1) % gif.n_frames

        new_frame = Image.new('RGBA', frame.size)

        if mode == 'partial':
            new_frame.paste(frame)

        new_frame.paste(frame, (0, 0), frame)

        result_frame_path = os.path.join(output_folder, f"{adjusted_frame_number:05d}.png")
        new_frame.save(result_frame_path, 'PNG')

    gif.close()
    

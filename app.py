import rembg
import gradio

def image_background_removal(input_img):
    output_path = 'output.png'
    output = rembg.remove(input_img)
    output.save(output_path)
    return output_path

demo = gradio.Interface(image_background_removal, gradio.Image(type='pil'), 'image')
demo.launch(share=True)
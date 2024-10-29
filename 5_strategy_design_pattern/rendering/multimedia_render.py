from abc import ABC, abstractmethod
import pygame
import pygame_gui
from moviepy.editor import *


# Base Render Class with abstract render method

class WidgetRender(ABC):
    @abstractmethod
    def render(self, screen, ui_manager):
        pass


#Image Render class inherits from WidgetRender
class ImageRender(WidgetRender):
    def __init__(self, image_path, size=None):
        self.image_path = image_path  #Path of image file
        self.image = None  #Image object to hold
        self.size = size  #Desired size fot the image (width,height)

    def load_image(self):
        self.image = pygame.image.load(self.image_path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def render(self, screen, ui_manager):
        if not self.image:
            self.load_image()

        screen.blit(self.image, (200, 70))
        return "RENDERING AN IMAGE", None


class VideoRender(WidgetRender):
    def __init__(self, video_path, size=None):
        self.video_path = video_path  #    Path of video file
        self.clip = None  #to hold video object
        self.playing = False  #flag to indicate if video is currently playing
        self.start_time = 0  # Timestamp for when the video starts playing
        self.size = size  # Desired size of the video (width,height)

    def load_video(self):
        self.clip = VideoFileClip(self.video_path)
        if self.clip:
            self.clip=self.clip.resize(self.size)

    def render(self, screen, ui_manager):
        if not self.clip:
            self.load_video()
        current_time = pygame.time.get_ticks() / 1000
        if not self.playing:
            self.playing = True
            self.start_time = current_time

        if self.playing:
            elapsed_time = current_time - self.start_time
            if elapsed_time < self.clip.duration:

                frame = self.clip.get_frame(elapsed_time)
                frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                screen.blit(frame, (200, 70))
            else:
                self.playing = False
            return "RENDERING A VIDEO", None

    def stop(self):
        self.playing = False


class FormRender(WidgetRender):
    def __init__(self):
        self.form_elements = []  # to store form elements
        self.panel = None

    def create_form(self, ui_manager):
        self.panel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((300, 60), (260, 480)),
                                                 starting_height=1,
                                                 manager=ui_manager,
                                                 object_id="form_panel",
                                                 anchors={"left": "left", "right": "right", "top": "top", "bottom": "bottom"})

        self.form_elements.append(pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 10), (200, 30)),
            text='FirstName',
            manager=ui_manager, container=self.panel

        ))
        self.form_elements.append(pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((30, 40), (200, 30)),
            manager=ui_manager, container=self.panel)
        )

        self.form_elements.append(pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 70), (200, 30)),
            text='LastName',
            manager=ui_manager, container=self.panel
        ))
        self.form_elements.append(pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((30, 100), (200, 30)),
            manager=ui_manager, container=self.panel
        ))

    def render(self, screen, ui_manager):
        if not self.form_elements:
            self.create_form(ui_manager)
        return "Rendering Form", None

    def clear_form(self):
        for element in self.form_elements:
            element.kill()

        self.form_elements = []
        if self.panel:
            self.panel.kill()
            self.panel = None


class RenderingContext:
    """
    This code will not change if add more Rendering Services
    """

    def __init__(self, renderer: WidgetRender):
        self._renderer = renderer

    def set_renderer(self, renderer: WidgetRender):
        self._renderer = renderer

    def render(self, screen, ui_manager):
        return self._renderer.render(screen, ui_manager)


#
# Main function to set up and run the application.
#
def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Renderer Strategy Pattern Example")
    ui_manager = pygame_gui.UIManager((800, 600))

    # Initialize the RenderingContext with an ImageRenderer instance.
    context = RenderingContext(ImageRender("demo.png", size=(550, 325)))

    # Create and configure UI buttons for selecting renderers.
    #
    image_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (100, 40)),
                                                text="Image",
                                                manager=ui_manager)
    video_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 70), (100, 40)),
                                                text="Video",
                                                manager=ui_manager)
    widget_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 120), (100, 40)),
                                                 text="Widget",
                                                 manager=ui_manager)

    rendered_widget = None

    clock = pygame.time.Clock()
    running = True
    while running:
        # calculate the delta time in seconds by asking for a max number of frames per second
        # to be 60 and then divide the tick time (which is in milliseconds) by a 1000 to get
        # elapsed time in seconds
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Process button click events and change the renderer accordingly.
            #
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isinstance(context._renderer, FormRender):
                        context._renderer.clear_form()
                    if event.ui_element == image_button:
                        context.set_renderer(ImageRender("demo.png", size=(550, 325)))
                    elif event.ui_element == video_button:
                        context.set_renderer(VideoRender("rabbit.mp4", size=(550, 325)))
                    elif event.ui_element == widget_button:
                        context.set_renderer(FormRender())

            ui_manager.process_events(event)

        # Update the screen and UI elements.
        screen.fill((200, 200, 200))
        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)

        # Call the render method of the current context.
        result_text, widget = context.render(screen, ui_manager)

        # Display the result text on the screen.
        font = pygame.font.Font(None, 36)
        text = font.render(result_text, 1, (10, 10, 10))
        screen.blit(text, (300, 20))

        # Update the rendered widget.
        if rendered_widget:
            rendered_widget.kill()
        if widget:
            rendered_widget = widget

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

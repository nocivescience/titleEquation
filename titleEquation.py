from manim import *
import itertools
class TituloScene(Scene):
    def construct(self):
        titulo=Text("Ecuaciones diferenciales parciales" ,t2c={"diferenciales":RED,"Ecuaciones":BLUE, "parciales":YELLOW}, font="NOTO SERIF", weight="BOLD").set(width=config["frame_width"]-1).to_edge(UP)
        self.play(Write(titulo))
        self.wait(10)
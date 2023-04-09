from manim import *


def high_integral_sums(amount):  # rectangles amount in single-period interval
    int_sum = 0
    for k in range(1, (amount * 6) + 1):
        int_sum += (((k / (amount * 2)) ** 2) * (1 / (amount * 2)))
    return str(round(int_sum, 3))


def low_integral_sums(amount):
    int_sum = 0
    for k in range(1, (amount * 6) + 1):
        int_sum += ((((k - 1) / (amount * 2)) ** 2) * (1 / (amount * 2)))
    return str(round(int_sum, 3))


def center_integral_sums(amount):
    int_sum = 0
    for k in range(1, (amount * 6) + 1):
        int_sum += ((((k - (1 / 2)) / (amount * 2)) ** 2) * (1 / (amount * 2)))
    return str(round(int_sum, 3))


class LabAnimation(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E
        start = MathTex(r'\text{Laboratory Work №1}', font_size=48, color=WHITE).shift(UP * 0.4)
        topic = MathTex(r'\text{Riemann Integrals}', font_size=48, color=WHITE).move_to(start).shift(DOWN)
        self.play(Write(start))
        self.play(Write(topic))
        self.wait(0.3)
        self.play(FadeOut(start, topic))
        self.wait(0.2)

        #  partition with left-side framing
        left_side = MathTex(r'\text{Partition with Left-Side Framing}', font_size=48, color=WHITE)
        self.play(Write(left_side))
        self.wait(0.3)
        self.play(FadeOut(left_side))
        self.wait(0.2)

        ax = Axes(
            x_range=[-3.3, 0.5], y_range=[-0.5, 10.2], tips=True,
            axis_config={
                "include_numbers": False,
                "color": WHITE,
                "include_ticks": False
            },
        )
        labels = ax.get_axis_labels(x_label="x", y_label='y')
        labels.color = WHITE
        self.play(Create(ax), Create(labels))

        A = ax.x_axis.get_tick(-3, size=0.1)
        a_label = Tex("$-3$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({-3: a_label})
        b_label = Tex("$0$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({0: b_label}, direction=DOWN * 0.8 + RIGHT * 0.8)
        C = ax.y_axis.get_tick(9, size=0.1)
        c_label = Tex("$9$", color=WHITE, font_size=24)
        ax.y_axis.add_labels({9: c_label}, direction=RIGHT)
        self.play(Create(A), Create(C), Create(a_label), Create(b_label), Create(c_label))
        self.wait(0.5)

        graph = ax.plot(lambda x: x ** 2, x_range=[-3, 0.3], color=WHITE)
        self.play(Create(graph))

        tex = MathTex(r'f(x)=x^2, \; x \in [-3, 0]', font_size=36, color=WHITE).shift(RIGHT + UP * 2)
        self.play(Write(tex))

        int_sums_left = []

        for i in range(1, 6):
            rects = ax.get_riemann_rectangles(
                graph,
                x_range=[-3, 0],
                dx=1 / (2 * i),
                color=(PURPLE_D, RED_B, MAROON_A),
                input_sample_type="left",
                fill_opacity=0.85
            )
            int_sums_left.append(
                MathTex(r'\sigma_{\tau}(f,\xi)=' + high_integral_sums(i), font_size=36).move_to(
                    tex).shift(DOWN * 0.8))
            self.play(Create(rects))
            int_sums = int_sums_left[i - 1]
            self.play(Write(int_sums))
            self.wait(0.6)
            self.play(FadeOut(rects, int_sums))
            self.wait(0.2)

        self.play(FadeOut(graph, labels, ax, tex, A, C))
        self.wait(0.8)

        #  partition with right-side framing
        right_side = MathTex(r'\text{Partition with Right-Side Framing}', font_size=48, color=WHITE)
        self.play(Write(right_side))
        self.wait(0.3)
        self.play(FadeOut(right_side))
        self.wait(0.2)

        ax = Axes(
            x_range=[-3.3, 0.5], y_range=[-0.5, 10.2], tips=True,
            axis_config={
                "include_numbers": False,
                "color": WHITE,
                "include_ticks": False
            },
        )
        labels = ax.get_axis_labels(x_label="x", y_label='y')
        labels.color = WHITE
        self.play(Create(ax), Create(labels))

        A = ax.x_axis.get_tick(-3, size=0.1)
        a_label = Tex("$-3$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({-3: a_label})
        b_label = Tex("$0$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({0: b_label}, direction=DOWN * 0.8 + RIGHT * 0.8)
        C = ax.y_axis.get_tick(9, size=0.1)
        c_label = Tex("$9$", color=WHITE, font_size=24)
        ax.y_axis.add_labels({9: c_label}, direction=RIGHT)
        self.play(Create(A), Create(C), Create(a_label), Create(b_label), Create(c_label))
        self.wait(0.5)

        graph = ax.plot(lambda x: x ** 2, x_range=[-3, 0.3], color=WHITE)
        self.play(Create(graph))

        self.play(Write(tex))

        int_sums_left = []

        for i in range(1, 6):
            rects = ax.get_riemann_rectangles(
                graph,
                x_range=[-3, 0],
                dx=1 / (2 * i),
                color=(DARK_BLUE, BLUE_B, TEAL),
                input_sample_type="right",
                fill_opacity=0.85
            )
            int_sums_left.append(
                MathTex(r'\sigma_{\tau}(f,\xi)=' + low_integral_sums(i), font_size=36).move_to(
                    tex).shift(DOWN * 0.8))
            self.play(Create(rects))
            int_sums = int_sums_left[i - 1]
            self.play(Write(int_sums))
            self.wait(0.6)
            self.play(FadeOut(rects, int_sums))
            self.wait(0.2)

        self.play(FadeOut(graph, labels, ax, tex, A, C))
        self.wait(0.8)

        # partition with center framing
        center = MathTex(r'\text{Partition with Center Framing}', font_size=48, color=WHITE)
        self.play(Write(center))
        self.wait(0.3)
        self.play(FadeOut(center))
        self.wait(0.2)

        ax = Axes(
            x_range=[-3.3, 0.5], y_range=[-0.5, 10.2], tips=True,
            axis_config={
                "include_numbers": False,
                "color": WHITE,
                "include_ticks": False
            },
        )
        labels = ax.get_axis_labels(x_label="x", y_label='y')
        labels.color = WHITE
        self.play(Create(ax), Create(labels))

        A = ax.x_axis.get_tick(-3, size=0.1)
        a_label = Tex("$-3$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({-3: a_label})
        b_label = Tex("$0$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({0: b_label}, direction=DOWN * 0.8 + RIGHT * 0.8)
        C = ax.y_axis.get_tick(9, size=0.1)
        c_label = Tex("$9$", color=WHITE, font_size=24)
        ax.y_axis.add_labels({9: c_label}, direction=RIGHT)
        self.play(Create(A), Create(C), Create(a_label), Create(b_label), Create(c_label))
        self.wait(0.5)

        graph = ax.plot(lambda x: x ** 2, x_range=[-3, 0.3], color=WHITE)
        self.play(Create(graph))

        self.play(Write(tex))

        int_sums_left = []

        for i in range(1, 6):
            rects = ax.get_riemann_rectangles(
                graph,
                x_range=[-3, 0],
                dx=1 / (2 * i),
                color=(PURE_RED, ORANGE, YELLOW_C),
                input_sample_type="center",
                fill_opacity=0.85
            )
            int_sums_left.append(
                MathTex(r'\sigma_{\tau}(f,\xi)=' + center_integral_sums(i), font_size=36).move_to(
                    tex).shift(DOWN * 0.8))
            self.play(Create(rects))
            int_sums = int_sums_left[i - 1]
            self.play(Write(int_sums))
            self.wait(0.6)
            self.play(FadeOut(rects, int_sums))
            self.wait(0.2)

        self.play(FadeOut(graph, labels, ax, tex, A, C))
        self.wait(0.8)
        conclusion = MathTex(r'\textbf{By the formula of Newton-Leibniz:', font_size=36, color=GOLD_B).shift(UP)
        riemann_int = MathTex(r'\int\limits_{-3}^{0} x^2 \; dx = \frac{x^3}{3} \Bigg |_{-3}^{0} = 9', font_size=42,
                              color=GREEN_C).move_to(conclusion).shift(DOWN * 1.2)
        self.play(Write(conclusion))
        self.wait(0.3)
        self.play(Write(riemann_int))
        self.wait(1)
        self.play(FadeOut(conclusion, riemann_int))
        self.wait(0.3)

        #  final statement
        ax = Axes(
            x_range=[-3.3, 0.5], y_range=[-0.5, 10.2], tips=True,
            axis_config={
                "include_numbers": False,
                "color": WHITE,
                "include_ticks": False
            },
        )
        labels = ax.get_axis_labels(x_label="x", y_label='y')
        labels.color = WHITE
        self.play(Create(ax), Create(labels))

        A = ax.x_axis.get_tick(-3, size=0.1)
        a_label = Tex("$-3$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({-3: a_label})
        b_label = Tex("$0$", color=WHITE, font_size=24)
        ax.x_axis.add_labels({0: b_label}, direction=DOWN * 0.8 + RIGHT * 0.8)
        C = ax.y_axis.get_tick(9, size=0.1)
        c_label = Tex("$9$", color=WHITE, font_size=24)
        ax.y_axis.add_labels({9: c_label}, direction=RIGHT)
        self.play(Create(A), Create(C), Create(a_label), Create(b_label), Create(c_label))
        self.wait(0.5)

        graph = ax.plot(lambda x: x ** 2, x_range=[-3, 0.3], color=WHITE)
        self.play(Create(graph))

        self.play(Write(tex))

        area = ax.get_area(
            graph,
            x_range=(-3, 0),
            color=GREEN_C,
            opacity=0.85,
        )

        statement = MathTex(r'\sigma_{\tau}(f,\xi)=\int\limits_{-3}^{0} x^2 \; dx=9', font_size=36,
                            color=GREEN_C).move_to(tex).shift(DOWN * 1.1)
        self.play(DrawBorderThenFill(area), run_time=1)
        self.play(Write(statement))
        self.wait(0.6)
        self.play(FadeOut(area, statement))
        self.play(FadeOut(graph, labels, ax, tex, A, C))
        self.wait(1)

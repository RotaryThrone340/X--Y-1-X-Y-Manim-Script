from manim import *

class NegativeExponents(Scene):
    def construct(self):
        def twrite_text(text, scale=1, pos=ORIGIN):
            text_obj = Text(text).scale(scale).move_to(pos)
            self.play(Write(text_obj))
            return text_obj

        def lwrite_latex(latex_str, scale=1, pos=ORIGIN, time=1):
            expr = MathTex(latex_str).scale(scale).move_to(pos)
            self.play(Write(expr), run_time=time)
            return expr

        def sdraw_shape(shape, *args, **kwargs):
            if shape == "Circle":
                obj = Circle(*args, **kwargs)
            elif shape == "Square":
                obj = Square(*args, **kwargs)
            elif shape == "Triangle":
                obj = Triangle(*args, **kwargs)
            elif shape == "Arrow":
                start = args[0] if len(args) > 0 else LEFT
                end = args[1] if len(args) > 1 else RIGHT
                obj = Arrow(start, end, **kwargs)
            else:
                raise ValueError(f"Shape '{shape}' not recognized.")

            self.play(Create(obj))
            return obj

        def delay(duration):
            self.wait(duration)

        def remove(items, time=1):
            self.play(*[Uncreate(item) for item in items], run_time=time)

        def morph(items, final_text, time=1, pos=None):
            if "\\" in final_text or "^" in final_text or "_" in final_text:
                target = MathTex(final_text).scale(1)
            else:
                target = Text(final_text).scale(1)

            if pos is None:
                pos = [0, 0, 0]
            target.move_to(pos)

            self.play(*[Transform(item, target.copy()) for item in items], run_time=time)
            self.remove(*items)
            self.add(target)
            return target

        def move(items_positions, time=1):
            self.play(*[item.animate.move_to(pos) for item, pos in items_positions], run_time=time)

        # Start animation sequence
        title = twrite_text("Hello! Today I will answer a confusing question.", 1, ORIGIN)
        move([(title, [0, 2, 0])])

        question = twrite_text("Why is the following true?", 0.7, ORIGIN)
        move([(question, [0, 1, 0])])

        equation = lwrite_latex(r"x^{-y} = \frac{1}{x^y}", 1, ORIGIN, 1)
        delay(2)

        remove([title, question, equation], time=0.3)

        txt = twrite_text("Now, we know that exponents is repeated multiplication.", 0.5, [0, 0.5, 0])
        delay(0.5)
        txt2 = lwrite_latex(r"x^4 = x \cdot x \cdot x \cdot x", 1, [0, -0.5, 0])
        delay(1)

        remove([txt, txt2], 1)

        txt = twrite_text("Let's start with this", 1, [0, 0.5, 0])
        txt2 = lwrite_latex(r"x^2 = x \cdot x", 1, [0, -0.5, 0])
        delay(1.5)

        remove([txt, txt2], 1)

        txt = twrite_text("If we then add 1 to the exponent,", 1, [0, 1, 0])
        txt2 = twrite_text("then it is the same as multiplying by x", 1, [0, 0, 0])
        delay(1)

        move([(txt, [0, 2, 0]), (txt2, [0, 1, 0])])

        equation = lwrite_latex(r"x^2 = x \cdot x")
        delay(0.25)

        equation = morph([equation], r"x^3 = x \cdot x \cdot x", time=1)
        delay(0.25)

        equation = morph([equation], r"x^4 = x \cdot x \cdot x \cdot x", time=1)
        delay(1)

        remove([equation, txt, txt2], 1)

        txt = twrite_text("Now if you instead remove from the exponent,", 1, [0, 0, 0])
        move([(txt, [0, 1, 0])])
        txt2 = twrite_text("then it is the same as division", 1, [0, 0, 0])
        move([(txt, [0, 2, 0]), (txt2, [0, 1, 0])])

        equation = lwrite_latex(r"x^4 = x \cdot x \cdot x \cdot x")
        delay(1)

        equation = morph([equation], r"x^3 = x \cdot x \cdot x \cdot x / x", time=1)
        delay(0.5)

        equation = morph([equation], r"x^3 = x \cdot x \cdot x", time=1)
        delay(1)

        equation = morph([equation], r"x^2 = x \cdot x \cdot x / x", time=1)
        delay(0.5)

        equation = morph([equation], r"x^2 = x \cdot x", time=1)
        delay(1)

        remove([txt, txt2, equation], 1)

        txt = twrite_text("Now watch what happens when we keep lowering the exponent", .5)
        delay(1)
        remove([txt], 1)

        equation = lwrite_latex(r"x^1 = x \cdot x / x")
        delay(0.5)

        equation = morph([equation], r"x^1 = x", time=1)
        delay(1)

        equation = morph([equation], r"x^0 = x / x", time=1)
        delay(0.5)

        equation = morph([equation], r"x^0 = 1", time=1)
        delay(1)

        equation = morph([equation], r"x^{-1} = 1/x", time=1)
        delay(.5)

        equation = morph([equation], r"x^{-1} = \frac{1}{x}", time=1)
        delay(1)

        equation = morph([equation], r"x^{-2} = \frac{1}{x} \div x", time=1)
        delay(0.5)

        equation = morph([equation], r"x^{-2} = \frac{1}{x^2}", time=1)
        delay(1)

        remove([equation], 1)

        txt = twrite_text("Now, if we put 2 from the previous equation as y,", 1, [0, 0, 0])
        move([
            (txt, [0, 1, 0])
        ])
        txt2 = twrite_text("then we get the following equation", 1, [0, 0, 0])
        move([
            (txt, [0, 2, 0]),
            (txt2, [0, 1, 0])
        ])
        equation = lwrite_latex(r"x^{-y} = \frac{1}{x^y}", 1)
        delay(1)

        remove([txt, txt2, equation], 1)

        txt = twrite_text("I hope this video helped you understand that little bit more math", 0.5)
        move([(txt, [0, 1, 0])])
        txt2 = twrite_text("Comment a question and I will likely make a video about it!", .5)

        delay(1)

        move([
            (txt, [0, -2, 0]),
            (txt2, [0, -3, 0])
        ])

        delay(4)
        self.play(FadeOut(txt, run_time=3), FadeOut(txt2, run_time=3))

from manim import *
import numpy as np

class CompleteSolution(Scene):
    def construct(self):
        # 第一部分：运算定义
        self.show_operation_definition()
        self.clear_scene()
        
        # 第二部分：问题描述
        self.show_problem_statement()
        self.clear_scene()
        
        # 第三部分：思考过程
        self.show_thinking_process()
        self.clear_scene()
        
        # 第四部分：奇偶性分析
        self.show_parity_analysis()
        self.clear_scene()
        
        # 第五部分：最大值分析
        self.show_max_value_analysis()
        self.clear_scene()
        
        # 第六部分：最终答案
        self.show_final_answer()
        self.clear_scene()
        
        # 第七部分：示例计算
        self.show_example_calculation()
        
        # 结尾
        self.show_ending()
    
    def clear_scene(self):
        """清空场景并添加过渡"""
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
    
    def show_operation_definition(self):
        """介绍运算定义"""
        title = Text("运算 ~ 的定义", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        definition = MathTex("a", "~", "b", "=", "|", "a", "-", "b", "|", font_size=36)
        definition.shift(UP * 0.5)
        self.play(Write(definition))
        self.wait(2)
        
        example_text = Text("例如:", font_size=30)
        example_text.next_to(definition, DOWN, buff=0.8)
        self.play(Write(example_text))
        
        examples = VGroup(
            MathTex("3", "~", "7", "=", "|3-7|", "=", "4", font_size=30),
            MathTex("5", "~", "2", "=", "|5-2|", "=", "3", font_size=30)
        )
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(example_text, DOWN, buff=0.5)
        
        for example in examples:
            self.play(Write(example))
            self.wait(0.5)
        
        self.wait(2)
    
    def show_problem_statement(self):
        """问题描述"""
        title = Text("问题描述", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        problem_lines = VGroup(
            Text("对于数字 1, 2, 3, ..., n (n > 4) 的不同排列", font_size=28),
            Text("依次进行运算: a₁ ~ a₂ ~ a₃ ~ ... ~ aₙ", font_size=28),
            Text("求所有排列中计算结果的最小值和最大值", font_size=28)
        )
        problem_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem_lines.shift(UP * 0.5)
        
        for line in problem_lines:
            self.play(Write(line))
            self.wait(0.5)
        
        self.wait(1)
        
        example_note = Text("例如: 1~2~3~4~5 与 5~4~3~2~1 结果不同", font_size=24, color=GREEN)
        example_note.next_to(problem_lines, DOWN, buff=0.8)
        self.play(Write(example_note))
        self.wait(2)
    
    def show_thinking_process(self):
        """思考过程"""
        title = Text("思考过程", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        steps = VGroup(
            Text("1. 分析运算性质: a~b = |a-b|", font_size=26),
            Text("2. 发现奇偶性规律", font_size=26),
            Text("3. 确定最小值与总和的奇偶性相关", font_size=26),
            Text("4. 通过案例分析最大值的模式", font_size=26),
            Text("5. 归纳出与 n mod 4 的关系", font_size=26)
        )
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        steps.shift(UP * 0.3)
        
        for step in steps:
            self.play(Write(step))
            self.wait(1)
        
        self.wait(2)
    
    def show_parity_analysis(self):
        """奇偶性分析"""
        title = Text("奇偶性分析", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        sum_formula = MathTex("S", "=", "1+2+\\cdots+n", "=", "\\frac{n(n+1)}{2}", font_size=36)
        sum_formula.shift(UP * 1.5)
        self.play(Write(sum_formula))
        self.wait(2)
        
        observation = Text("关键观察:", font_size=30, color=YELLOW)
        observation.next_to(sum_formula, DOWN, buff=0.8)
        self.play(Write(observation))
        
        key_insight = VGroup(
            Text("最终结果的奇偶性", font_size=26),
            Text("与总和 S 的奇偶性相同", font_size=26)
        )
        key_insight.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        key_insight.next_to(observation, DOWN, buff=0.5)
        
        self.play(Write(key_insight))
        self.wait(2)
        
        min_conclusion = VGroup(
            Text("因此最小值 min 为:", font_size=26),
            MathTex("\\text{min} = \\begin{cases} 0 & \\text{If } S \\text{ even} \\\\ 1 & \\text{If } S \\text{ odd} \\end{cases}", font_size=30)
        )
        min_conclusion.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        min_conclusion.next_to(key_insight, DOWN, buff=0.8)
        
        self.play(Write(min_conclusion))
        self.wait(3)
    
    def show_max_value_analysis(self):
        """最大值分析"""
        title = Text("最大值分析", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        cases_title = Text("通过案例分析发现规律:", font_size=30)
        cases_title.shift(UP * 1)
        self.play(Write(cases_title))
        
        cases = VGroup(
            Text("n   n mod 4  max", font_size=24, font="Monospace"),
            Text("5       1       5", font_size=24, font="Monospace"),
            Text("6       2       5", font_size=24, font="Monospace"), 
            Text("7       3       6", font_size=24, font="Monospace"),
            Text("8       0       8", font_size=24, font="Monospace")
        )
        cases.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        cases.next_to(cases_title, DOWN, buff=0.5)
        
        for case in cases:
            self.play(Write(case))
            self.wait(0.3)
        
        self.wait(2)
        
        pattern = Text("规律:", font_size=30, color=YELLOW)
        pattern.next_to(cases, DOWN, buff=0.8)
        self.play(Write(pattern))
        
        max_rule = MathTex("\\text{max} = \\begin{cases} n & \\text{If } n \\equiv 0,1 \\pmod{4} \\\\ n-1 & \\text{If } n \\equiv 2,3 \\pmod{4} \\end{cases}", font_size=36)
        max_rule.next_to(pattern, DOWN, buff=0.5)
        
        self.play(Write(max_rule))
        self.wait(3)
    
    def show_final_answer(self):
        """最终答案"""
        title = Text("最终答案", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        min_formula = MathTex("\\text{min} = \\begin{cases} 0 & \\text{If } \\frac{n(n+1)}{2} \\text{ even} \\\\ 1 & \\text{else} \\end{cases}", font_size=36)
        min_formula.shift(UP * 0.5)
        self.play(Write(min_formula))
        self.wait(2)
        
        max_formula = MathTex("\\text{max} = \\begin{cases} n & \\text{If } n \\equiv 0,1 \\pmod{4} \\\\ n-1 & \\text{If } n \\equiv 2,3 \\pmod{4} \\end{cases}", font_size=36)
        max_formula.next_to(min_formula, DOWN, buff=0.8)
        self.play(Write(max_formula))
        self.wait(2)
        
        note = Text("以上结果对于 n > 4 成立", font_size=24, color=GREEN)
        note.next_to(max_formula, DOWN, buff=0.8)
        self.play(Write(note))
        self.wait(3)
    
    def show_example_calculation(self):
        """示例计算"""
        title = Text("示例: n=5 的计算", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        info = VGroup(
            MathTex("n=5, \\quad S = \\frac{5\\times6}{2} = 15", font_size=30),
            MathTex("S \\text{ is odd} \\Rightarrow \\text{min} = 1", font_size=30),
            MathTex("5 \\equiv 1 \\pmod{4} \\Rightarrow \\text{max} = 5", font_size=30)
        )
        info.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        info.shift(UP * 0.5)
        
        for item in info:
            self.play(Write(item))
            self.wait(1)
        
        self.wait(2)
    
    def show_ending(self):
        """结尾"""
        ending_text = Text("谢谢观看!", font_size=60, color=GOLD)
        self.play(Write(ending_text))
        self.wait(2)
        
        # 渐出效果
        self.play(FadeOut(ending_text))
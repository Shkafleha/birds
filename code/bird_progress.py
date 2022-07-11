from IPython.display import display, HTML

class ProgressBox:
    def __init__(self, stages=None, total_files=0):
        stages = stages if stages else {}
        self.process_stages = stages
        self.stages = {"load":0} 
        [self.stages.update({s:i+1}) for i,s in enumerate(stages)]
        self.stages.update({'save':len(stages)+1, 'ok':len(stages)+2})
        self.box = display(HTML("ждите, готовимся..."), display_id=True)
        self.total = total_files

    def _html(self):
        load, load_op = ("......", 0.6) if self.stages[self.stage]==0 else ("✔", 1)
        save, save_op = ("", 0.2) if self.stages[self.stage]<len(self.stages)-2 else ("......", 0.6) if self.stages[self.stage]==len(self.stages)-2 else ("✔", 1)
        op, flag = [], []
        html = f"""
            <span style='weight:bold;font-size:16pt'>{self.count:03d}/{self.total:03d}</span><br>
            <span style='opacity:{load_op}'>загружаем <b>{self.file}</b> {load}</span><br>
        """
        for i, (s,t) in enumerate(self.process_stages.items()):
            f, o = ("", 0.2) if self.stages[self.stage]<1+i else ("......", 0.6) if self.stages[self.stage]==1+i else ("✔", 1)
            flag.append(f)
            op.append(o)
            html += f"<span style='opacity:{op[i]}'>{t} {flag[i]}</span><br>"
        html += f"<span style='opacity:{save_op}'>сохраняем результат {save}</span>"
        return HTML(html)

    def new_file(self, file, count):
        self.file = file
        self.count = count
        self.stage = 'load'
        self.box.update(self._html())
    
    def new_stage(self, stage):
        self.stage = stage
        self.box.update(self._html())
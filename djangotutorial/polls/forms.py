from django import forms

NB_MAX_CHOIX = 5


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label="Question text",
        max_length=200,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(NB_MAX_CHOIX):
            self.fields[f"choix_{i}"] = forms.CharField(
                label=f"Choice #{i + 1}",
                max_length=200,
                required=False
            )
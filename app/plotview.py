import matplotlib.pyplot as plt
import seaborn as sns

class PlotView:
    def __init__(self):
        pass

    def display_chart(self, data, x, y, st):
        fig = plt.figure()
        ax = sns.barplot(data=data, x=x, y=y, palette='rocket')
        st.pyplot(fig)
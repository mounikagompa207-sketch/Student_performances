import plotly.express as px


def score_chart(score):

    fig = px.bar(

        x=["Performance"],

        y=[score],

        text=[score],

        title="Student Performance Score"

    )

    fig.update_traces(textposition="outside")

    return fig


def attendance_chart(attendance):

    fig = px.pie(

        values=[attendance, 100-attendance],

        names=["Present", "Absent"],

        hole=0.5,

        title="Attendance"

    )

    return fig
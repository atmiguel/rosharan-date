import streamlit as st

from roshar.rosharan.date import RosharanDate
from typing import Optional


def display_integer_input(
    *,
    default: int,
    key: Optional[str] = None,
    label: str,
    max: Optional[int] = None,
    min: Optional[int] = None,
) -> int:
    return st.number_input(
        key=key,
        label=label,
        max_value=max,
        min_value=min,
        step=1,
        value=default,
    )


def display_date_input(*, initial_date: RosharanDate) -> RosharanDate:
    columns = st.columns(4)

    with columns[0]:
        year = display_integer_input(
            default=initial_date.year,
            label="Year",
        )

    with columns[1]:
        month = display_integer_input(
            default=initial_date.month,
            label="Month",
            max=RosharanDate.MAX_MONTH,
            min=RosharanDate.MIN_MONTH,
        )

    with columns[2]:
        # TODO: on change that pairs inputs together
        week = display_integer_input(
            default=initial_date.week,
            label="Week",
            max=RosharanDate.MAX_WEEK,
            min=RosharanDate.MIN_WEEK,
        )

        # # TODO: on change that pairs inputs together
        # st.selectbox(
        #     label="Week Name",
        #     options=[number.name for number in RosharanNumber],
        #     index=week - 1,
        # )

    with columns[3]:
        day = display_integer_input(
            default=initial_date.day,
            label="Day",
            max=RosharanDate.MAX_DAY,
            min=RosharanDate.MIN_DAY,
        )

    return RosharanDate(
        year=year,
        month=month,
        week=week,
        day=day,
    )


if __name__ == "__main__":
    st.title("Rosharan Date")

    # From https://roshar.17thshard.com/#/en-US/events/kaladin-joins-bridge-four:
    # 1173.7.9.3 - Kaladin joins Bridge Four
    initial_date = RosharanDate(1173, 7, 9, 3)

    # TODO(adrian@gradient.ai, 04/05/2024): make a selector to choose how dates will be entered
    period_name = st.selectbox(
        label="Name",
        options=["Day", "Week", "Month"],
    )

    match period_name:
        case "Day":
            year = display_integer_input(
                default=initial_date.year,
                key="day_name_year",
                label="Year",
            )

            day_names = list(RosharanDate.list_all_day_names().keys())
            day_name = st.selectbox(
                label="Day Name",
                options=day_names,
                index=day_names.index(initial_date.get_day_name()),
            )

            date = RosharanDate.from_day_name(
                day_name=day_name,
                year=year,
            )
        case "Week":
            pass
        case "Month":
            pass
        case _:
            raise Exception(f"period_name unexpected: {period_name}")

    st.write(f"Date id: {date}")
    st.write(f"Month name: {date.get_month_name()}")
    st.write(f"Week name: {date.get_week_name()}")
    st.write(f"Day name: {date.get_day_name()}")

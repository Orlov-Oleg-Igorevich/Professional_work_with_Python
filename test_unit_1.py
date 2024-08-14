import pytest
import winners
import who_next
import dating

@pytest.fixture
def preparation():
    print('\nStart test')
    yield
    print('\nEnd test')

@pytest.mark.parametrize('list_,expected', (
    [[123, 145, 346, 246, 235, 166, 112, 351, 436], ([346, 166, 436], 3)],
    [[123, 145], ([], 0)]
    ))
def test_task_winner(preparation, list_, expected):
    result, count = winners.solve(list_)
    assert (result, count) == expected, f"Список или количество чеков неверны. \
                                                    Ожидание: {expected}, реальность: {result, count}."
    

@pytest.mark.parametrize(
    'hare_list,turtle_list,expected',
    (
        [[8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], "черепаха"],
        [[8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], "заяц"],
        [[8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], "одинаково"]
    )
)
def test_task_nest(preparation, hare_list, turtle_list, expected):
    result = who_next.solve(hare_list, turtle_list)
    assert result == expected, f"Победитель определен неверно. \
                                Ожидалось: {expected}, получено: {result}."
    

@pytest.mark.parametrize(
    'boy_list,girl_list,expected',
    (
        [['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha"],
        [['Peter', 'Alex', 'John', 'Arthur'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], "Кто-то может остаться без пары!"]
    )
)
def test_task_dating(preparation, boy_list, girl_list, expected):
    result = dating.solve(boy_list, girl_list)
    assert result ==expected, f"Знакомство не удалось: {result}"

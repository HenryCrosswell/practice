from practice.main import main, two_sum


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from practice!\n"


def test_two_sum_found():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_not_found():
    assert two_sum([1, 2, 3], 100) == []


def test_two_sum_multiple_pairs():
    assert two_sum([3, 2, 4], 6) == [1, 2]

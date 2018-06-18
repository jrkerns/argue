import unittest

import argue


@argue.options(blob=('thing1', 'thing2'))
def select(blob):
    return blob


@argue.options(blob=('thing1', 'thing2'), color=('red', 'green'))
def select2(blob, color):
    return blob, color


class TestOptions(unittest.TestCase):

    def test_invalid_keyword_str(self):
        with self.assertRaises(ValueError):
            select(blob='thing3')

    def test_valid_str_passes(self):
        self.assertEqual(select(blob='thing1'), 'thing1')

    def test_positional_str(self):
        self.assertEqual(select('thing1'), 'thing1')

    def test_positional_invalid_str(self):
        with self.assertRaises(ValueError):
            select('thing3')

    def test_multiple_options(self):
        self.assertEqual(select2('thing1', 'red'), ('thing1', 'red'))


@argue.bounds(first=(0, 3))
def add(first, second):
    return first + second


@argue.bounds(f=(0, 2), s=(3, 4))
def add2(f, s):
    return f + s


class TestBounds(unittest.TestCase):

    def test_valid_value(self):
        self.assertEqual(add(first=2, second=5), 7)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            add(first=9, second=5)

    def test_valid_positional_value(self):
        self.assertEqual(add(2, 4), 6)

    def test_invalid_positional_value(self):
        with self.assertRaises(ValueError):
            add(4, 1)

    def test_non_number_range_fails(self):
        with self.assertRaises(TypeError):
            @argue.bounds(f=(0, '5'))
            def add(f, s):
                pass

    def test_multiple_ranges(self):
        self.assertEqual(add2(1, 3), 4)

    def test_3_range_values_fails(self):
        with self.assertRaises(ValueError):
            @argue.bounds(f=(0, 1, 2))
            def q(f):
                pass


class ConditionalClass:
    a = False

    def do_first(self):
        self.a = True

    @argue.conditional(a=True)
    def do_second(self):
        pass


class TestConditional(unittest.TestCase):

    def test_valid_condition_passes(self):
        c = ConditionalClass()
        c.do_first()
        c.do_second()  # shouldn't raise

    def test_invalid_condition_fails(self):
        c = ConditionalClass()
        with self.assertRaises(ValueError):
            c.do_second()


class TestCombos(unittest.TestCase):

    def test_all_three(self):

        class C:
            a = False

            def do_first(self):
                self.a = True

            @argue.conditional(a=True)
            @argue.options(arg=(1, 2, 3))
            @argue.bounds(arg=(1, 3))
            def do_second(self, arg):
                pass

        c = C()
        c.do_first()
        c.do_second(2)












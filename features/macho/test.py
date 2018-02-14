from regression_tests import *

class TestX86C(Test):
    settings = CriticalTestSettings(
        input='hello.x86.clang.macho',
    )

    def test_has_main_function(self):
        assert self.out_c.has_func( 'main' )

class TestX86Cpp(Test):
    settings = CriticalTestSettings(
        input='hello.cpp.x86.clang.macho',
    )

    def test_has_main_function(self):
        assert self.out_c.has_func( 'main' )

class TestArmC(Test):
    settings = CriticalTestSettings(
        input='hello.arm.clang.macho',
    )

    def test_pass(self):
        pass

class TestArmCpp(Test):
    settings = CriticalTestSettings(
        input='hello.cpp.arm.clang.macho',
    )

    def test_pass(self):
        pass

class TestAckMacho(Test):
    settings = TestSettings(
        # We need to use a compiled binary as the input because we check
        # function addresses in the test (the addresses depend on the used
        # compiler and thus may differ from system to system).
        input='ack.x86.clang.macho'
    )

    def test_has_main_function(self):
        assert self.out_c.has_func( 'main' )

    def test_decompilation_has_funcs(self):
        assert self.out_c.has_func( '_ack' )
        assert self.out_c.has_func( 'function_1eee' )

    def test_decompilation_calls(self):
        assert self.out_c.funcs['_ack'].calls( '_ack' )
        assert self.out_c.funcs['function_1eee'].calls( '_scanf', '_ack', '_printf' )
#pragma once
#include "test.hpp"

void test_raw()
{
    RawAllocator ba;
    auto ptr = ba.allocate(1);
    expect(ptr != nullptr) << "RawAllocator::allocate() returned nullptr";
    ba.deallocate(ptr);
}

void test_base()
{
    "base"_test = [] {
        test_raw();
    };
}
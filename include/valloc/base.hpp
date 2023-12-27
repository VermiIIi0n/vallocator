#ifndef _VALLOC_BASE_HPP
#define _VALLOC_BASE_HPP

#include <cstddef>
#include <cstdint>
#include <stdexcept>
#include <type_traits>
#include <concepts>
#include <utility>

namespace vermils
{
namespace valloc
{
    using std::size_t;
    using std::uint8_t;
    using std::uintptr_t;
    using std::bad_alloc;

    class bad_dealloc : public std::exception {};

    class BaseAllocator
    {
    public:
        virtual ~BaseAllocator() = default;
        virtual void* allocate(size_t size) = 0;
        virtual void deallocate(void* ptr) = 0;
    };

    class RawAllocator : public BaseAllocator
    {
    public:
        void* allocate(size_t size) override
        {
            return new uint8_t[size];
        }
        void deallocate(void* ptr) override
        {
            delete[] reinterpret_cast<uint8_t*>(ptr);
        }
    };
}
}

#endif
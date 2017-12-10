#include <asio.hpp>
#include <chrono>
#include <cstdio>

int main()
{
	asio::io_service io;

	asio::steady_timer t(io, std::chrono::seconds(0));
	t.wait();

	std::puts("Hello, world!");

	return 0;
}
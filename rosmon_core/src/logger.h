// Logs all output to a log file for the run
// Author: Max Schwarz <max.schwarz@uni-bonn.de>

#ifndef LOGGER_H
#define LOGGER_H

#include <memory>
#include <string>

#include "log_event.h"

namespace rosmon
{

class Logger
{
public:
	virtual ~Logger() = default;
	virtual void log(const LogEvent& event) = 0;
};

/**
 * @brief Write log messages into a log file
 **/
class FileLogger : public Logger
{
public:
	/**
	 * @brief Constructor
	 *
	 * @param path Path to the output file
	 **/
	explicit FileLogger(const std::string& path, bool flush = false);
	~FileLogger() override;

	//! Log message
	void log(const LogEvent& event) override;
private:
	FILE* m_file = nullptr;
	bool m_flush = false;
};

/**
 * @brief Write log messages to syslog
 **/
class SyslogLogger : public Logger
{
public:
	explicit SyslogLogger(const std::string& launchFileName);

	void log(const LogEvent& event) override;

private:
	std::string m_tag;
};

/**
 * @brief Write log messages to systemd journal
 **/
class SystemdLogger : public Logger
{
public:
	class NotAvailable : public std::runtime_error
	{
	public:
		NotAvailable(const std::string& msg)
		 : std::runtime_error{msg}
		{}
	};

	explicit SystemdLogger(const std::string& launchFileName);
	~SystemdLogger() override;

	void log(const LogEvent& event) override;

private:
	std::string m_launchFileName;
	int m_fd = -1;
};

}

#endif

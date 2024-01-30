#!/usr/bin/env ruby

log_file_path = ARGV[0]

# Check if the log file path is provided
unless log_file_path
  puts "Usage: ./100-textme.rb <log_file_path>"
  exit 1
end

# Regular expression to extract sender, receiver, and flags from the log entry
regex = /\[from:(\S+)\] \[to:(\S+)\] \[flags:([^\]]+)\]/

# Read the log file and process each line
File.foreach(log_file_path) do |line|
  match_data = line.match(regex)
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]

    # Output the result in the required format
    puts "#{sender},#{receiver},#{flags}"
  end
end

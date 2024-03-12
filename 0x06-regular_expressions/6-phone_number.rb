#!/usr/bin/env ruby

regex = /^\d{10}$/

ARGV.each do |arg|
  match = arg.scan(regex).join
  puts match
end    

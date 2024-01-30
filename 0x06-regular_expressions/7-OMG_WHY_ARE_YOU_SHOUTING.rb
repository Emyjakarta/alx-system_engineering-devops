#!/usr/bin/env ruby

regex = /[A-Z]/

ARGV.each do |arg|
  match = arg.scan(regex).join
  puts match
end    

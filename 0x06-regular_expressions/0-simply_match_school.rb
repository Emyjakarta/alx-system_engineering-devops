#!/usr/bin/env ruby

regex = /School/

ARGV.each do |argv|
  match = argv.scan(regex).join
  puts match
end

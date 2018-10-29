# https://www.ruby-toolbox.com/projects/roo
# Roo can do Excel, CSV, OpenOffice, LibreOffice formats
#
# gem install roo
require 'roo'


new_xlsx = Roo::Excelx.new('./sample.xlsx')
puts new_xlsx.info



existing_xlsx = Roo::Spreadsheet.open('./sample.xlsx', extension: :xlsx)
puts existing_xlsx.info
puts existing_xlsx.sheets
puts existing_xlsx.sheet(0).row(1)
puts existing_xlsx.sheet(0).column(1)
puts existing_xlsx.cell(1,1)
puts existing_xlsx.cell('A',1)
puts existing_xlsx.a1


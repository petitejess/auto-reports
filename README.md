# Auto Reports

Automating manual reports using Excel templates from MYOB exports.

## 🚧 Under Construction 🚧 

Converting stand alone python scripts to automate report generation...

Coming soon... 🙌

My python app report generator is coming soon, so I can automate more stuff! Soon. 🤭

### Current Stage

For now, to test the terminal app out, rename the below files (remove "_sample"):    

| Path | Original File Name | New File Name |
| ---- | ----------------- | ------------- |
| app/configs/ | companyconfig_sample.json | companyconfig.json |
| app/configs/ | inputfileconfig_sample.json | inputfileconfig.json |
| app/configs/ | orderslookupconfig_sample.json | orderslookupconfig.json |
| app/configs/ | eomslookupconfig_sample.json | eomslookupconfig.json |
| app/inputdir/ | ITEMSALE_sample.TXT | ITEMSALE.TXT |
| app/templates/eoms/ | eoms_template_sample.xlsx | eoms_template.xlsx |


In the root directory */app/*, you can now run: 
* To generate Orders:    
`python app.py orders`
* To generate End of Month Statements:    
`python app.py eoms`

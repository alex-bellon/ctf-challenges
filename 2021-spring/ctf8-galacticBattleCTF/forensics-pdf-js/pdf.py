from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
ipdf = PdfFileReader(open('original.pdf', 'rb'))

for i in range(ipdf.getNumPages()):
	page = ipdf.getPage(i)
	output.addPage(page)

with open('out.pdf', 'wb') as f:
    output.addJS("var _0x790b=['\x32\x38\x31\x35\x38\x38\x67\x6a\x48\x79\x61\x43','\x31\x31\x38\x38\x35\x31\x77\x47\x41\x6c\x71\x74','\x31\x31\x34\x35\x31\x31\x39\x48\x48\x73\x52\x53\x44','\x35\x32\x34\x38\x34\x32\x4c\x7a\x65\x41\x48\x66','\x38\x33\x6e\x78\x4a\x67\x52\x76','\x32\x38\x35\x30\x36\x39\x48\x43\x73\x4b\x76\x63','\x38\x38\x39\x55\x71\x4d\x61\x49\x54','\x31\x44\x58\x67\x4d\x56\x52','\x31\x34\x34\x36\x37\x37\x6c\x55\x59\x48\x64\x4e'];var _0x407b=function(_0x294226,_0x4a3243){_0x294226=_0x294226-0x136;var _0x790b45=_0x790b[_0x294226];return _0x790b45;};(function(_0x1a3463,_0x59bc93){var _0x230651=_0x407b;while(!![]){try{var _0x1470d5=-parseInt(_0x230651(0x13b))+-parseInt(_0x230651(0x13e))*parseInt(_0x230651(0x137))+parseInt(_0x230651(0x136))+-parseInt(_0x230651(0x13d))+-parseInt(_0x230651(0x139))+-parseInt(_0x230651(0x13a))+-parseInt(_0x230651(0x13c))*-parseInt(_0x230651(0x138));if(_0x1470d5===_0x59bc93)break;else _0x1a3463['push'](_0x1a3463['shift']());}catch(_0x56827b){_0x1a3463['push'](_0x1a3463['shift']());}}}(_0x790b,0x45eeb),console['\x6c'+'\x6f'+'\x67']('\x75'+'\x74'+'\x66'+'\x6c'+'\x61'+'\x67'+'\x7b'+'\x62'+'\x65'+'\x5f'+'\x63'+'\x61'+'\x72'+'\x65'+'\x66'+'\x75'+'\x6c'+'\x5f'+'\x77'+'\x69'+'\x74'+'\x68'+'\x5f'+'\x70'+'\x64'+'\x66'+'\x73'+'\x7d'));")
    output.write(f)

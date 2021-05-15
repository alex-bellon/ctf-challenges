# Secret Transmission
* **Event:** galacticBattleCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The prompt mentions that the PDF was somehow made to run code. If you inspect the PDF using something like `strings` or `pdfinfo`, you will see that there is some JavaScript code embedded in the file (PDFs can run JavaScript!):

```javascript
var _0x790b=['281588gjHyaC','118851wGAlqt','1145119HHsRSD','524842LzeAHf','83nxJgRv','285069HCsKvc','889UqMaIT','1DXgMVR','144677lUYHdN'];var _0x407b=function(_0x294226,_0x4a3243){_0x294226=_0x294226-0x136;var _0x790b45=_0x790b[_0x294226];return _0x790b45;};(function(_0x1a3463,_0x59bc93){var _0x230651=_0x407b;while(!![]){try{var _0x1470d5=-parseInt(_0x230651(0x13b))+-parseInt(_0x230651(0x13e))*parseInt(_0x230651(0x137))+parseInt(_0x230651(0x136))+-parseInt(_0x230651(0x13d))+-parseInt(_0x230651(0x139))+-parseInt(_0x230651(0x13a))+-parseInt(_0x230651(0x13c))*-parseInt(_0x230651(0x138));if(_0x1470d5===_0x59bc93)break;else _0x1a3463['push'](_0x1a3463['shift']());}catch(_0x56827b){_0x1a3463['push'](_0x1a3463['shift']());}}}(_0x790b,0x45eeb),console['l'+'o'+'g']('u'+'t'+'f'+'l'+'a'+'g'+'{'+'b'+'e'+'_'+'c'+'a'+'r'+'e'+'f'+'u'+'l'+'_'+'w'+'i'+'t'+'h'+'_'+'p'+'d'+'f'+'s'+'}'));
```

#### Step 2
If you run this JavaScript, it will give you the flag (or you can just read it from the code since it's hardcoded): `utflag{be_careful_with_pdfs}`.

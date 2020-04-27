// v8n.bg9X = function(Z9Q, e8e) {
//         var i8a = {}
//           , e8e = NEJ.X({}, e8e)
//           , me2x = Z9Q.indexOf("?");
//         if (window.GEnc && /(^|\.com)\/api/.test(Z9Q) && !(e8e.headers && e8e.headers[ev0x.BL6F] == ev0x.Jm8e) && !e8e.noEnc) {
//             if (me2x != -1) {
//                 i8a = k8c.gW1x(Z9Q.substring(me2x + 1));
//                 Z9Q = Z9Q.substring(0, me2x)
//             }
//             if (e8e.query) {
//                 i8a = NEJ.X(i8a, k8c.fM1x(e8e.query) ? k8c.gW1x(e8e.query) : e8e.query)
//             }
//             if (e8e.data) {
//                 i8a = NEJ.X(i8a, k8c.fM1x(e8e.data) ? k8c.gW1x(e8e.data) : e8e.data)
//             }
//             i8a["csrf_token"] = v8n.gM1x("__csrf");
//             Z9Q = Z9Q.replace("api", "weapi");
//             e8e.method = "post";
//             delete e8e.query;
//             var bVj7c = window.asrsea(JSON.stringify(i8a), brx9o(["流泪", "强"]), brx9o(Xs4w.md), brx9o(["爱心", "女孩", "惊恐", "大笑"]));
//             e8e.data = k8c.cx9o({
//                 params: bVj7c.encText,
//                 encSecKey: bVj7c.encSecKey
//             })
//         }
//         cxt3x(Z9Q, e8e)
//     }

var CryptoJS = require("crypto-js");
// console.log(CryptoJS.HmacSHA1("Message", "Key"));
function charToHex(a) {
    var h, b = 48, c = b + 9, d = 97, e = d + 25, f = 65, g = 90;
    return h = a >= b && c >= a ? a - b : a >= f && g >= a ? 10 + a - f : a >= d && e >= a ? 10 + a - d : 0
}
function hexToDigit(a) {
    var d, b = 0, c = Math.min(a.length, 4);
    for (d = 0; c > d; ++d)
        b <<= 4,
        b |= charToHex(a.charCodeAt(d));
    return b
}
function biFromHex(a) {
    var d, e, b = new BigInt, c = a.length;
    for (d = c,
    e = 0; d > 0; d -= 4,
    ++e)
        b.digits[e] = hexToDigit(a.substr(Math.max(d - 4, 0), Math.min(d, 4)));
    return b
}
function RSAKeyPair(a, b, c) {
    this.e = biFromHex(a),
    this.d = biFromHex(b),
    this.m = biFromHex(c),
    this.chunkSize = 2 * biHighIndex(this.m),
    this.radix = 16,
    this.barrett = new BarrettMu(this.m)
}
function BigInt(a) {
    this.digits = "boolean" == typeof a && 1 == a ? null : ZERO_ARRAY.slice(0),
    this.isNeg = !1
}

function setMaxDigits(a) {
    maxDigits = a,
    ZERO_ARRAY = new Array(maxDigits);
    for (var b = 0; b < ZERO_ARRAY.length; b++)
        ZERO_ARRAY[b] = 0;
    bigZero = new BigInt,
    bigOne = new BigInt,
    bigOne.digits[0] = 1
}
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }

    // function d(d,e,f,g)
    //
    // {var h={},i=a(16);
    // return h.encText=b(d,g),h.encText=b(h.encText,i),h.encSecKey=c(i,e,f),h
    //
    // }

    console.log(d(1,2,3,3))
<!--
目的: LDPC符号について理解する
キーワード: unknown...😇
-->

**LDPC(Low-Density Parity-Check)符号**は、1960年代にGallagerによって発見されました。
この符号が注目されるようになったのは30年以上後の1990年代から[^1]ですが、この再発見により符号理論界にブレイクスルーを起こしました。
現在では、LDPC符号はイーサネットや衛星通信、LTEやWiFiにおける誤り訂正方式として標準化されています。

これほど注目されるようになった大きな理由は、その復号方式によります。
LDPC符号の復号方式は、そのタナ―グラフ(Tanner Graph)が疎であることを活用して確率伝搬アルゴリズム(belief propagation algorithm)[^2]と呼ばれる方法を使って復号します。
それによって、非常に良いパフォーマンスで復号することが可能になります。
また、適切に符号を設定するとシャノン限界に迫る特性を達成することも大きな理由の一つとして挙げられます。

# LDPC符号の定義 -Definition of LDPC Codes
まずは本題のLDPC符号の定義を紹介します。

#### 定義 1.1
$H$を${\mathbb F}_2$上の行列とする。$H$の成分に1が少ないとき、$H$を**疎行列(sparse matrix)**といい、
疎行列$H$をパリティ検査行列にもつ線形符号$C$と疎行列$H$のペア$(C, H)$を**LDPC符号(Low-Density Parity-Check Codes)**という。
<br/><br/>

$(C, H)$を単に$C$と書くこともありますが、符号$C$から得られた$H$が疎行列であることは必ずしも言えないため、$C$だけを指してLDPC符号と呼ぶのは好ましくないとされています。

次にLDPC符号の復号法で重要な役割を持っているタナ―グラフを見ていきます。
タナ―グラフは行列$H$から表される二部グラフのことで、次のように定義されます。

#### 定義 1.2
$H=(h_{i,j})$をサイズが$m\times n$の${\mathbb F}_2$上の行列として、集合$V_c,V_v$をそれぞれ$V_c := \{c_1, c_2, \dots, c_m\}, V_v := \{v_1, v_2, \dots, v_n\}$とする。

集合$V,E$をそれぞれ

\begin{eqnarray}
V &:=& V_c \cup V_v\\
E &:=& \{(c_i, v_j)\in V_c\times V_v\ |\ h_{i,j}=1\}
\end{eqnarray}

としたとき、二部グラフ$(V,E)$を**タナ―グラフ(Tanner Graph)**という。また、$V_c$の元を**検査ノード(check nodes)**、$V_v$の元を**変数ノード(variable nodes)**という。

# 参考文献
- 井坂元彦,「知識の森」6章 ターボ符号・LDPC符号, _電子情報通信学会_, 2012
- 萩原学, 符号理論, _日本評論社_, 2012
- Marco Baldi, QC-LDPC Code-Based Cryptography, _Springer_, 2014
- IEEE, Enhancing the error-correcting performance of LDPC codes for LTE and WiFi, https://ieeexplore.ieee.org/abstract/document/7148600, 2015

[^1]: 当時では、符号長が大きいと計算量が莫大になるなどの理由によって影を潜めていたそうです
[^2]: sum-product復号法とも言います。ターボ符号(1993~, turbo codes)もこの復号法を使うことができるため注目されています。
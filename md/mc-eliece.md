<!--
目的: McEliece暗号について理解する
キーワード: 構成方法、安全性、information set decoding
-->

**耐量子計算機暗号**または**耐量子暗号** (PQC：post-quantum cryptography) の候補として注目を集めている**符号ベース暗号** (CBC：code-based cryptography)。
その中でも原始的かつ実用的な**McEliece暗号** (McEliece cryptosystem) についてまとめました。

# 準備 - Preparetion

$R$を可換環とするとき、R上の$m\times n$行列全体の集合を$R^{m\times n}$と表す。
また、正方行列の各行および各列について、成分の一つが1でありそれ以外の成分が0であるとき、その行列を**置換行列** (permutation matrix) とよぶ。
なお、$n$次の置換行列$P$について、$j$列目の成分1がある場所を$\sigma(j)$行目とすると、$\sigma$は集合$\{1, 2, \ldots, n\}$からそれ自身への全単射 ($n$文字の置換) を定める。
このように置換$\sigma$に対応する置換行列$P$を考えると、逆写像$\sigma^{-1}$に対応する置換行列が$P$の逆行列となる。

# 構成方法 - Protocol

## Definition 1.1 McEliece暗号 (McEliece cryptosystem)

McEliece暗号$\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$は以下のように構成される：

- $\mathrm{Gen}(1^{\kappa})$は、セキュリティパラメータ$\kappa$に応じて、復号が効率的な何らかの誤り訂正符号$C$を選び、その生成行列$G_{0}\in K^{k\times n}$をつくる。
  この誤り訂正符号$C$の復号アルゴリズムを$\mathrm{Dcd}$、誤り訂正能力を$t$とする。
  次に、正則な$k$次正方行列$S$と、$n$次の置換行列$P$をランダムに選び、$G\coloneqq SG_{0}P\in K^{k\times n}$を計算する。そして、公開鍵$\mathrm{pk}$と秘密鍵$\mathrm{sk}$を以下のように定める：
  $$\mathrm{pk}\leftarrow(G, t); \mathrm{sk}\leftarrow(S, G_{0}, P, \mathrm{Dcd})$$
  対応する平文空間は$\mathcal{M} = K^{k}$、暗号空間は$\mathcal{C} = K^{n}$とする。

- $\mathrm{Enc}_{\mathrm{pk}}(m) (m\in\mathcal{M})$は、Hamming重み$t$のベクトル$e\in K^{n}$をランダムに選び、暗号文$c\in K^{n}$を以下のように定める：
  $$c\leftarrow mG + e.$$

- $\mathrm{Dec}_{\mathrm{sk}}(c) (c\in\mathcal{C})$は、まず、ベクトル$c'\leftarrow CP^{-1}\in K^{n}$を計算し、それを誤り訂正符号$C$の受信メッセージだと思って復号した結果$w\leftarrow \mathrm{Dcd}(c')$を計算する。
  次に、連立方程式$w = m'G_{0}$を解いてベクトル$m'\in K^{k}$を得る。
  そして$\tilde{m}\leftarrow m'S^{-1}$を復号結果とする。

# 復号方法 - Decoding Protocol

<!-- Patterson's algorithmについて書く。 -->

# 安全性 - Security

<!-- information-set decoding に対しては? -->

# 参考文献 - References

1. Robert J。McEliece：A Public-Key Cryptosystem Based on Algebraic Coding Theory。*The Deep Space Network Progress Report、DSN PR 42-44*、pp.114-116、1978。

1. 縫田光司。耐量子計算機暗号。森北出版、東京、2020。

1. Marek Repka and Pierre-Louis Cayrel。Chpter 5 Cryptography Based on Error Correcting Codes: A Surevey、*Multidisciplinary Perspectives in Cryptology and Information Security*、pp.139-141、2014。

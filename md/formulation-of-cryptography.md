<!-- 
目的: 暗号技術の定式化について理解する
キーワード: 暗号化方式の定式化，セキュリティパラメータ
-->

# はじめに - Before You Read

本記事では暗号技術について評価・議論する際に必須となるいくつかの定式化 (formulation) についてまとめた．

# 準備 - Preparetion

## Def. セキュリティパラメータ (security parameter)

**セキュリティパラメータ** (security parameter) は，公開鍵や秘密鍵のサイズを決定する値である．
通常，この値を大きくすると安全性が強まるが代わりに効率性が低下するため，実際に利用する際には適当なパラメータの選択が必要となる．

**注**)
一般に，セキュリティパラメータは$\kappa$で表される．
例えば，$1^{\kappa}$は1を$\kappa$個並べた列 (つまり，$\underbrace{1 1 \dots 1}_{\kappa\mbox{個}}$) であり，鍵のサイズが$\kappa$ビットであることを表している．

# 様々な暗号化方式 - Various Cryptosystem

## Def. 共通鍵暗号化方式 (common-key cryptosystem)

**共通鍵暗号化方式** (common-key cryptosystem) または **秘密鍵暗号化方式** (secret-key cryptosystem)，**対称鍵暗号化方式** (symmetric-key cryptosystem) とは，以下の仕様を充たす確率的アルゴリズムの組$\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$のことと定める．
ここでそれぞれのアルゴリズムは，セキュリティパラメータに関する多項式時間アルゴリズムであるとする．

- **鍵生成** (key generation) **アルゴリズム**$\mathrm{Gen}$は，セキュリティパラメータ$\kappa$を入力とし，秘密鍵$\mathrm{sk}$を出力する：

$$\mathrm{sk} \leftarrow \mathrm{Gen}(1^{\kappa}).$$

- **暗号化** (encryption) **アルゴリズム**$\mathrm{Enc}$は，秘密鍵$\mathrm{sk}$と平文$m\in\mathcal{M}$を入力とし，暗号文$\mathrm{Enc}_{\mathrm{sk}}(m) = c\in\mathcal{C}$を出力する：

$$c \leftarrow \mathrm{Enc}_{\mathrm{sk}}(m).$$

- **復号** (decryption) **アルゴリズム**$\mathrm{Dec}$は，秘密鍵$\mathrm{sk}$と暗号文$c\in\mathcal{C}$を入力とし，平文$\mathrm{Dec}_{\mathrm{sk}}(c) = m'\in\mathcal{M}$あるいは$\perp$ (復号が失敗したことを表す) のいずれかを出力する：

$$m' \leftarrow \mathrm{Dec}_{\mathrm{sk}}(c)\ \mbox{または} \perp \leftarrow \mathrm{Dec}_{\mathrm{sk}}(c).$$

## Def. 公開鍵暗号化方式 (public-key cryptosystem)

**公開鍵暗号化方式** (public-key cryptosystem) とは，以下の仕様を充たす確率的アルゴリズムの組$\Pi = (\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$のことと定める．
ここでそれぞれのアルゴリズムは，セキュリティパラメータに関する多項式時間アルゴリズムであるとする．

- **鍵生成アルゴリズム**$\mathrm{Gen}$は，セキュリティパラメータ$\kappa$を入力とし，公開鍵$\mathrm{pk}$と秘密鍵$\mathrm{sk}$の対 (これを「鍵対 (かぎつい)」ともよぶ) を出力する：

$$(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathrm{Gen}(1^{\kappa}).$$

- **暗号化アルゴリズム**$\mathrm{Enc}$は，公開鍵$\mathrm{pk}$と平文$m\in\mathcal{M}$を入力とし，暗号文$\mathrm{Enc}_{\mathrm{pk}}(m) = c\in\mathcal{C}$を出力する：

$$c \leftarrow \mathrm{Enc}_{\mathrm{pk}}(m).$$

- **復号アルゴリズム**$\mathrm{Dec}$は，秘密鍵$\mathrm{sk}$と暗号文$c\in\mathcal{C}$を入力とし，平文$\mathrm{Dec}_{\mathrm{sk}}(c) = m'\in\mathcal{M}$あるいは$\perp$のいずれかを出力する：

$$m' \leftarrow \mathrm{Dec}_{\mathrm{sk}}(c)\ \mbox{または} \perp \leftarrow \mathrm{Dec}_{\mathrm{sk}}(c).$$

**注**)
上記の定義では復号アルゴリズムの入力に公開鍵$\mathrm{pk}$は含まれないが，実際の方式においては復号時に公開鍵の情報も必要となることがある．
そのため，暗号分野の文献では，復号アルゴリズムの入力が公開鍵を含んでいると暗に仮定している場合が多い．$\Box$

# 参考文献 - References

1. IPUSIRON，暗号技術のすべて，翔泳社，2017．

1. 縫田光司，耐量子計算機暗号，森北出版，2020．

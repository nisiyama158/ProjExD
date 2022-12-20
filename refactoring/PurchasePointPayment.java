import java.time.LocalDateTime;

class PurchasePointPayment {
  final CustomerId customerId;          // 購入者のID
  final ComicId comicId;                // 購入するWebコミックのID
  final PurchasePoint consumptionPoint; // 購入で消費するポイント
  final LocalDateTime paymentDateTime;  // 購入日時

  PurchasePointPayment(final Customer customer, final Comic comic) {
    if (customer.isEnabled()) {
      customerId = customer.id;
      if (comic.isEnabled()) {
        comicId = comic.id;
        if (comic.currentPurchasePoint.amount <= customer.possessionPoint.amount) {
          consumptionPoint = comic.currentPurchasePoint;
          paymentDateTime = LocalDateTime.now();
        }
        else {
          throw new RuntimeException("所持ポイントが不足しています。");
        }
      }
      else {
        throw new IllegalArgumentException("現在取り扱いのできないコミックです。");
      }
    }
    else {
      throw new IllegalArgumentException("有効な購入者ではありません。");
    }
  }
}

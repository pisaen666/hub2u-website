/*
  ไฟล์ตั้งค่า Hub2U: เติมข้อมูลจริงที่นี่ไฟล์เดียว แล้วทุกหน้าจะเปลี่ยนตามเอง
  ช่องที่ยังเป็น "" (ว่าง) เว็บจะแสดงเป็นป้าย [ใส่...] สีส้มอ่อนให้เห็นว่ายังต้องเติม
  ห้ามเติมข้อมูลลับหรือรหัสผ่านในไฟล์นี้ เพราะเว็บเปิดให้ทุกคนเห็นได้
*/
window.HUB2U = {
  // ลิงก์ต่างๆ (ถ้าว่าง ปุ่มจะพาไปหน้า "ติดต่อเรา" แทน)
  lineUrl: "",          // ลิงก์ไลน์ เช่น https://line.me/R/ti/p/@xxxx
  appUrl: "",           // ลิงก์เว็บแอปสั่งของ (ปุ่ม "เปิดหน้าสั่งของ")
  shopSignupUrl: "",    // ลิงก์สมัครร้านค้า
  riderSignupUrl: "",   // ลิงก์สมัครไรเดอร์

  // ข้อมูลติดต่อ
  phone: "",            // เช่น 0812345678
  lineId: "",           // เช่น @hub2u
  hours: "",            // เวลาทำการ
  hubLocation: "",      // ตำแหน่งจุดรวมของในตลาด
  lineQrImage: "",      // ที่อยู่ไฟล์รูป QR ไลน์ เช่น assets/img/line-qr.png

  // การสั่งซื้อ
  deliveryFee: "",
  orderCutoff: "",
  deliveryRounds: "",
  daysOff: "",
  outOfStock: "",
  cancelPolicy: "",

  // ร้านค้าและไรเดอร์
  shopFee: "",
  shopPayCycle: "",
  shopDocs: "",
  riderRate: "",
  riderPayCycle: "",
  riderDocs: "",

  // แบรนด์
  story: "",            // เรื่องราวว่าทำไมถึงทำ Hub2U
  aboutPhoto: ""        // ที่อยู่ไฟล์รูปเจ้าของ/ทีมงาน เช่น assets/img/team.jpg
};

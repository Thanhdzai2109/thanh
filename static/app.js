class Chatbox {
  constructor() {
    this.args = {
      openButton: document.querySelector(".chatbox__button"),
      chatBox: document.querySelector(".chatbox__support"),
      sendButton: document.querySelector(".send__button"),
    };

    this.state = false;
    this.messages = [];
  }
  display() {
    const { openButton, chatBox, sendButton } = this.args;

    openButton.addEventListener("click", () => this.toggleState(chatBox));

    sendButton.addEventListener("click", () => this.onSendButton(chatBox));

    const node = document.getElementById("in");
    node.addEventListener("keyup", ({ key }) => {
      if (key === "Enter") {
        this.onSendButton(chatBox);
      }
    });
  }
  toggleState(chatbox) {
    this.state = !this.state;

    // show or hides the box
    if (this.state) {
      chatbox.classList.add("chatbox--active");
    } else {
      chatbox.classList.remove("chatbox--active");
    }
  }

  onSendButton(chatbox) {
    var textField = document.getElementById("in");
    let text1 = textField.value;
    if (text1 === "") {
      return;
    }

    let msg1 = { name: "User", message: text1 };
    this.messages.push(msg1);

    fetch("http://127.0.0.1:5000/question", {
      method: "POST",
      body: JSON.stringify({ message: text1 }),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((r) => r.json())
      .then((r) => {
        let msg2 = {
          name: "Bot",
          message: r.answer,
          bmi: r.bmi,
          v1: r.vong1,
          v2: r.vong2,
          v3: r.vong3,
          skin: r.skinMess,
          point: r.pointSkin,
          l: r.lenSkin,
        };
        this.messages.push(msg2);
        this.updateChatText(chatbox);
        textField.value = "";
      })
      .catch((error) => {
        console.error("Error:", error);
        this.updateChatText(chatbox);
        textField.value = "";
      });
  }

  updateChatText(chatbox) {
    var html = "";
    this.messages
      .slice()
      .reverse()
      .forEach(function (item, index) {
        if (item.name === "Bot") {
          if (item.bmi > 0) {
            html +=
              '<div class="messages__item messages__item--visitor">' +
              item.message +
              "</div>";
            html +=
              '<div class="messages__item messages__item--visitor">' +
              "Chỉ số bmi của bạn là: " +
              item.bmi +
              ", " +
              "Vòng 1: " +
              item.v1 +
              ", " +
              "Vòng 2: " +
              item.v2 +
              ", " +
              "Vòng 3: " +
              item.v3 +
              "<br>" +
              "hãy chọn size quần áo cho phù hợp với kích thước cơ thể!" +
              "</div>";
          } else {
            if (item.skin[0] == "none") {
              if (item.l > 0) {
                html +=
                  '<div class="messages__item messages__item--visitor">' +
                  "Da của bạn thuộc loại: " +
                  item.point[0] +
                  "<br>" +
                  "Triệu chứng: " +
                  item.point[1] +
                  "<br>" +
                  "Để da đẹp hơn bạn cần: " +
                  item.point[2] +
                  "</div>";
              } else {
                html +=
                  '<div class="messages__item messages__item--visitor">' +
                  item.message +
                  "</div>";
              }
            } else {
              html +=
                '<div class="messages__item messages__item--visitor">' +
                item.skin +
                "</div>";
            }
          }
        } else {
          html +=
            '<div class="messages__item messages__item--operator">' +
            item.message +
            "</div>";
        }
      });

    const chatmessage = chatbox.querySelector(".chatbox_messages");
    chatmessage.innerHTML = html;
  }
}
const chatbox = new Chatbox();
chatbox.display();

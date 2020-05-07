function createForm() {
        // create & name Form
        var item = "Version_2020-05-07_17-48-49";
        var form = FormApp.create(item).setTitle(item);
        // Page 1
        var Page1 = form.addPageBreakItem().setTitle("Herzlich Willkommen zur Online-Hausarbeitshilfe!");
        var item1 = form.addMultipleChoiceItem();
        // Page 2
        var Page2 = form.addPageBreakItem().setTitle("Halt stop!").setHelpText("Hier solltest du nicht sein!");
        // Page 3
        var Page3 = form.addPageBreakItem().setTitle("You're on a good way!").setHelpText("Prima.");
        // Page 4
        var Page4 = form.addPageBreakItem().setTitle("You‘re on a bad way!").setHelpText("Schade.");
        // end page
        var endPage = form.addPageBreakItem().setTitle("Bis bald!").setHelpText("Hoffentlich konnte ich dir helfen!");
        item1.setTitle("Hast du ein genaues Thema?").setChoices([item1.createChoice('Ja', Page3), item1.createChoice('Nein', Page4)]).setRequired(true);
        Page2.setGoToPage(FormApp.PageNavigationType.SUBMIT);
        Page3.setGoToPage(FormApp.PageNavigationType.SUBMIT);
        Page4.setGoToPage(FormApp.PageNavigationType.SUBMIT);
        endPage.setGoToPage(FormApp.PageNavigationType.SUBMIT);
}
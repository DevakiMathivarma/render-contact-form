from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process form data here
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash('Your message has been sent successfully!', 'success')
        return render_template('success.html', name=name)
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

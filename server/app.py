import os
import pandas as pd
from flask import Flask, request, render_template,session,redirect, url_for
from flask_cors import CORS
from urllib.parse import urlparse
import joblib
import re



app = Flask(__name__)
CORS(app)
app.secret_key = "safelinker123" 

# --- Correct model path ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../model/xgb_model.pkl")
model = joblib.load(MODEL_PATH)

# Features used during training
FEATURE_COLUMNS = [
    'length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens', 'nb_at', 'nb_qm',
    'nb_and', 'nb_or', 'nb_eq', 'nb_underscore', 'nb_tilde', 'nb_percent', 'nb_slash',
    'nb_star', 'nb_colon', 'nb_comma', 'nb_semicolumn', 'nb_dollar', 'nb_space',
    'nb_www', 'nb_com', 'nb_dslash', 'http_in_path', 'https_token', 'ratio_digits_url',
    'ratio_digits_host', 'punycode', 'port', 'tld_in_path', 'tld_in_subdomain',
    'abnormal_subdomain', 'nb_subdomains', 'prefix_suffix', 'random_domain',
    'shortening_service', 'path_extension', 'nb_redirection', 'nb_external_redirection',
    'length_words_raw', 'char_repeat', 'shortest_words_raw', 'shortest_word_host',
    'shortest_word_path', 'longest_words_raw', 'longest_word_host', 'longest_word_path',
    'avg_words_raw', 'avg_word_host', 'avg_word_path', 'phish_hints', 'domain_in_brand',
    'brand_in_subdomain', 'brand_in_path', 'suspecious_tld', 'statistical_report',
    'nb_hyperlinks', 'ratio_intHyperlinks', 'ratio_extHyperlinks', 'ratio_nullHyperlinks',
    'nb_extCSS', 'ratio_intRedirection', 'ratio_extRedirection', 'ratio_intErrors',
    'ratio_extErrors', 'login_form', 'external_favicon', 'links_in_tags', 'submit_email',
    'ratio_intMedia', 'ratio_extMedia', 'sfh', 'iframe', 'popup_window', 'safe_anchor',
    'onmouseover', 'right_clic', 'empty_title', 'domain_in_title',
    'domain_with_copyright', 'whois_registered_domain', 'domain_registration_length',
    'domain_age', 'web_traffic', 'dns_record', 'google_index', 'page_rank'
]



def extract_features_from_url(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    path = parsed.path

    features = {}

    # Core features
    features['length_url'] = len(url)
    features['length_hostname'] = len(hostname)
    features['ip'] = 1 if re.match(r'^\d+\.\d+\.\d+\.\d+$', hostname) else 0
    features['nb_dots'] = url.count('.')
    features['nb_hyphens'] = url.count('-')
    features['nb_at'] = url.count('@')
    features['nb_qm'] = url.count('?')
    features['nb_and'] = url.count('&')
    features['nb_or'] = url.count('|')
    features['nb_eq'] = url.count('=')
    features['nb_underscore'] = url.count('_')
    features['nb_tilde'] = url.count('~')
    features['nb_percent'] = url.count('%')
    features['nb_slash'] = url.count('/')
    features['nb_star'] = url.count('*')
    features['nb_colon'] = url.count(':')
    features['nb_comma'] = url.count(',')
    features['nb_semicolumn'] = url.count(';')
    features['nb_dollar'] = url.count('$')
    features['nb_space'] = url.count(' ')
    features['nb_www'] = url.count('www')
    features['nb_com'] = url.count('com')
    features['nb_dslash'] = url.count('//')

    # Tokens
    features['http_in_path'] = 1 if 'http' in path else 0
    features['https_token'] = 1 if 'https' in hostname else 0
    features['ratio_digits_url'] = sum(c.isdigit() for c in url) / len(url)
    features['ratio_digits_host'] = sum(c.isdigit() for c in hostname) / len(hostname) if len(hostname) > 0 else 0
    features['punycode'] = 1 if 'xn--' in hostname else 0
    features['port'] = 1 if ':' in hostname else 0

    # Subdomain / TLD checks
    features['tld_in_path'] = 1 if re.search(r'\.[a-z]{2,3}', path) else 0
    features['tld_in_subdomain'] = 1 if hostname.count('.') > 2 else 0
    features['abnormal_subdomain'] = 1 if hostname.count('.') > 3 else 0
    features['nb_subdomains'] = hostname.count('.') - 1 if hostname.count('.') > 1 else 0
    features['prefix_suffix'] = 1 if '-' in hostname else 0
    features['random_domain'] = 0  # needs external check
    features['shortening_service'] = 1 if any(s in url for s in ['bit.ly', 'tinyurl', 'goo.gl']) else 0

    # Path & redirections
    features['path_extension'] = 1 if re.search(r'\.[a-zA-Z]{2,4}', path) else 0
    features['nb_redirection'] = url.count('//') - 1
    features['nb_external_redirection'] = 0  # needs external request

    # Placeholders (need advanced extraction or external APIs)
    for col in [
        'length_words_raw', 'char_repeat', 'shortest_words_raw', 'shortest_word_host',
        'shortest_word_path', 'longest_words_raw', 'longest_word_host', 'longest_word_path',
        'avg_words_raw', 'avg_word_host', 'avg_word_path', 'phish_hints',
        'domain_in_brand', 'brand_in_subdomain', 'brand_in_path', 'suspecious_tld',
        'statistical_report', 'nb_hyperlinks', 'ratio_intHyperlinks', 'ratio_extHyperlinks',
        'ratio_nullHyperlinks', 'nb_extCSS', 'ratio_intRedirection', 'ratio_extRedirection',
        'ratio_intErrors', 'ratio_extErrors', 'login_form', 'external_favicon', 'links_in_tags',
        'submit_email', 'ratio_intMedia', 'ratio_extMedia', 'sfh', 'iframe', 'popup_window',
        'safe_anchor', 'onmouseover', 'right_clic', 'empty_title', 'domain_in_title',
        'domain_with_copyright', 'whois_registered_domain', 'domain_registration_length',
        'domain_age', 'web_traffic', 'dns_record', 'google_index', 'page_rank'
    ]:
        features[col] = 0
    for col in FEATURE_COLUMNS:
        features.setdefault(col, 0)

    return features


@app.route('/')
def index():
    result = session.pop('result', None)
    return render_template("index.html", result=result)


@app.route('/predict', methods=['POST'])
def predict():
    user_url = request.form.get('url')
    features = extract_features_from_url(user_url)

    # Convert to DataFrame
    X_new = pd.DataFrame([features])

    # Ensure correct order
    X_new = X_new.reindex(columns=FEATURE_COLUMNS, fill_value=0)

    # Prediction
    prediction = model.predict(X_new)

    if prediction[0] == 1:
        result = "⚠️ This link is likely FRAUDULENT."
    else:
        result = "✅ This link appears SAFE."

    session['result'] = result
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)

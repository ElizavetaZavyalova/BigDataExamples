CREATE TABLE IF NOT EXISTS mock_datach1
(
    id Int32,
    lab String,
    ok String
)
ENGINE = MergeTree()
ORDER BY id;
INSERT INTO mock_datach1 (id, lab, ok) VALUES
(1, 'AliceCh', 'yes'),
(2, 'BobCH', 'no'),
(3, 'CharlieCH', 'yes'),
(4, 'DianaCH', 'no'),
(5, 'EveCH', 'yes');
CREATE TABLE IF NOT EXISTS mock_datach2
(
    id Int32,
    lab String,
    ok String
)
ENGINE = MergeTree()
ORDER BY id;